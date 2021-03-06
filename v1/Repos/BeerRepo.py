import v1.Repos.SQL as SQL
from v1.Entity.Beer import Beer
from v1.DTO.TrueFalseDTO import TrueFalseDTO
from v1.DTO.QuantityDTO import QuantityDTO


from v1.DTO.TimeDistributionDTO import TimeDistributionDTO

class BeerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BeerRepo, self).__init__()
	
	def getAllBeers(self):
		sql = "Select * from Beer"
		items = self.query(sql,Beer)
		return items

	def getBarsWhichSoldTheMost(self,beer):
		sql = "SELECT bar AS name, total_start-total_end AS amount \
				FROM \
				(SELECT bar, SUM(startquantity) AS total_start, SUM(endquantity) AS total_end \
				FROM Inventory  \
				WHERE beer = \""+str(beer)+"\" \
				GROUP BY bar) s \
				ORDER BY amount \
				LIMIT 10"
		items = self.query(sql,QuantityDTO)
		return items


	def getBiggestConsumers(self,beer):
		sql = "SELECT b.drinker as name, SUM(t.quantity) AS amount\
				FROM Transactions t, Bills b \
				WHERE t.bill_id = b.bill_id AND t.item = \""+str(beer)+"\" \
				GROUP BY b.drinker \
				ORDER BY amount DESC \
				LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items

	def getTimeDistrubition(self,beer):
		sql = "SELECT m.morning_avg_sold AS morning_avg_sold, a.afternoon_avg_sold AS afternoon_avg_sold, \
			e.evening_avg_sold AS evening_avg_sold, n.night_avg_sold AS night_avg_sold \
			FROM \
			(SELECT AVG(s.num_sold) as morning_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.time >= \""+str("08:00")+"\" AND b.time < \""+str("12:00")+"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id AND t.item = \""+str(beer)+"\" \
			GROUP BY b1.date) s) m, \
			(SELECT AVG(s.num_sold) as afternoon_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.time >= \""+str("12:00")+"\" AND b.time < \""+str("16:00")+"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id AND t.item = \""+str(beer)+"\" \
			GROUP BY b1.date) s) a, \
			(SELECT AVG(s.num_sold) as evening_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.time >= \""+str("16:00")+"\" AND b.time < \""+str("20:00")+"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id AND t.item = \""+str(beer)+"\" \
			GROUP BY b1.date) s) e, \
			(SELECT AVG(s.num_sold) as night_avg_sold \
			FROM \
			(SELECT SUM(t.quantity) AS num_sold \
			FROM \
			(SELECT *  \
			FROM Bills b \
			WHERE b.time >= \""+str("20:00")+"\" AND b.time < \""+str("24:00")+"\") b1, \
			Transactions t \
			WHERE b1.bill_id = t.bill_id AND t.item = \""+str(beer)+"\" \
			GROUP BY b1.date) s) n;" 
		items = self.query(sql,TimeDistributionDTO)
		return items

	def insertBeer(self,Beer):
		sql = "INSERT INTO Beer (name, manf) VALUES (%s,%s)"
		vals = (Beer.getName(),Beer.getManf())
		return self.insert(sql,vals)

	def updateBeer(self,Beer,oldName):
		sql = "UPDATE Beer SET name = %s, manf = %s WHERE name = %s "
		vals = (Beer.getName(),Beer.getManf(), oldName)
		return self.update(sql,vals)

	def deleteBeer(self,Beer):
		sql = "DELETE FROM Beer WHERE name = %s "
		vals = (Beer.getName(),)
		return self.delete(sql,vals)
	
	def beer_exists(self, beer):
		sql = "SELECT EXISTS(SELECT * FROM Beer WHERE name = \""+str(beer)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
