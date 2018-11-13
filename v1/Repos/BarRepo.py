import v1.Repos.SQL as SQL

from v1.DTO.QuantityDTO import QuantityDTO
from v1.Entity.Bar import Bar
from v1.DTO.PeriodDistributionDTO import PeriodDistributionDTO
from v1.DTO.TimeDistributionDTO import TimeDistributionDTO
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class BarRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BarRepo, self).__init__()

	def getAllBars(self):
		sql = "Select * from Bar"
		items = self.query(sql,Bar)
		return items
	
	def getTop10RankBySalesOfManf(self, manf):
		sql = "SELECT  bar AS name, SUM(startquantity) - SUM(endquantity) AS amount \
		FROM Inventory i, (SELECT name AS beer FROM Beer WHERE manf = \""+str(manf)+"\") b \
		WHERE i.beer = b.beer \
		GROUP BY i.bar \
		ORDER BY amount DESC \
		LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items
	
	def getTop10RankBySalesForDay(self,day):
		sql = "SELECT bar AS name, SUM(startquantity) - SUM(endquantity) AS amount \
		FROM Inventory \
		WHERE dayname(date) = \""+str(day)+"\" \
		GROUP BY bar \
		ORDER BY amount DESC \
		LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items

	def getAllFractionsOfInventory(self, bar):
		sql = "SELECT dayname(date) as name, AVG(fraction_sold) as amount \
				FROM (SELECT beer, date, (total_start - total_end)/total_start AS fraction_sold \
				FROM (SELECT beer, date, SUM(startquantity) AS total_start, SUM(endquantity) AS total_end \
				FROM Inventory \
				WHERE bar = \""+str(bar)+"\" \
				GROUP BY date) s) s1 \
				GROUP BY name \
				ORDER BY dayofweek(date);"
		items = self.query(sql,QuantityDTO)
		return items

	def getbarTopBeerBrand(self,bar,dayOfWeek):
		sql = "SELECT manf AS name, SUM(quantity) AS amount \
				FROM Beer b RIGHT JOIN \
				(SELECT t.item AS item, SUM(t.quantity) AS quantity\
				FROM (SELECT * \
				FROM Bills b \
				WHERE b.bar = \""+str(bar)+"\" and b.day = \""+str(dayOfWeek)+"\") b, Transactions t \
				WHERE b.bill_id = t.bill_id AND type = \""+str("beer")+"\" \
				GROUP BY t.item) q ON q.item = b.name \
				GROUP BY manf \
				ORDER BY quantity DESC \
				LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items


	def getTopLargestSpenders(self,bar):
		sql = "SELECT b.drinker AS name, SUM(b.total_price) AS amount \
				FROM (SELECT * \
				FROM Bills \
				WHERE bar = \""+str(bar)+"\") b \
				GROUP BY b.drinker \
				ORDER BY amount DESC \
				LIMIT 10; "
		items = self.query(sql,QuantityDTO)
		return items


	def getSaleDistributionDays(self,bar):
		sql = "SELECT s.day AS period, AVG(s.num_sold) AS amount \
				FROM (SELECT SUM(t.quantity) AS num_sold, b1.date AS date, b1.day AS day \
				FROM (SELECT * \
				FROM Bills b \
				WHERE b.bar = \""+str(bar)+"\") b1, \
				Transactions t \
				WHERE b1.bill_id = t.bill_id \
				GROUP BY b1.date) s \
				GROUP BY s.day \
				ORDER BY dayofweek(s.date);"
		# sql = "SELECT b.day AS period, COUNT(b.bill_id) AS amount \
		# 		FROM (SELECT * \
		# 		FROM Bills \
		# 		WHERE bar = \""+str(bar)+"\") b \
		# 		GROUP BY b.day \
		# 		ORDER BY dayofweek(b.date);"
		items = self.query(sql,PeriodDistributionDTO)
		return items


	def getTimeDistrubition(self,bar):
		sql = "SELECT m.morning_avg_sold AS morning_avg_sold, a.afternoon_avg_sold AS afternoon_avg_sold, \
			e.evening_avg_sold AS evening_avg_sold, n.night_avg_sold AS night_avg_sold \
			FROM \
			(SELECT AVG(s.num_sold) as morning_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.bar = \""+str(bar)+"\" AND b.time >= \"" +str("08:00")+ "\" AND b.time < \"" +str("12:00")+ "\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id \
			GROUP BY b1.date) s) m, \
			(SELECT AVG(s.num_sold) as afternoon_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.bar = \""+str(bar)+"\" AND b.time >= \""+ str("12:00") + "\" AND b.time < \""+ str("16:00") +"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id \
			GROUP BY b1.date) s) a, \
			(SELECT AVG(s.num_sold) as evening_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.bar = \""+str(bar)+"\" AND b.time >= \"" +str("16:00") + "\" AND b.time < \""+str("20:00")+ "\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id \
			GROUP BY b1.date) s) e, \
			(SELECT AVG(s.num_sold) as night_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.bar =\""+str(bar)+"\" AND b.time >= \""+str("20:00")+"\" AND b.time < \""+str("24:00")+"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id \
			GROUP BY b1.date) s) n;"

		items = self.query(sql,TimeDistributionDTO)
		return items

	def insertBar(self,bar):
		sql = "INSERT INTO Bar (name, state) VALUES (%s,%s)"
		vals = (bar.getName(),bar.getState())
		return self.insert(sql,vals)


	def updateBar(self,bar,oldName):
		sql = "UPDATE Bar SET name = %s, state = %s WHERE name = %s "
		vals = (bar.getName(), bar.getState(), oldName)
		return self.update(sql,vals)

	def deleteBar(self,bar):
		sql = "DELETE FROM Bar WHERE name = %s "
		vals = (bar.getName(),)
		return self.delete(sql,vals)

	def bar_exists(self, bar):
		sql = "SELECT EXISTS(SELECT * FROM Bar WHERE name = \""+str(bar)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False