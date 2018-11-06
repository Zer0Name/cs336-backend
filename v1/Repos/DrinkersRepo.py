import v1.Repos.SQL as SQL
from v1.Entity.Drinker import Drinker
from v1.DTO.DrinkerTransactionDTO import DrinkerTransactionDTO
from v1.DTO.QuantityDTO import QuantityDTO
from v1.DTO.PeriodDistributionDTO import PeriodDistributionDTO

class DrinkerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(DrinkerRepo, self).__init__()

	def getAllDrinkers(self):
		sql = "Select * from Drinker"
		items = self.query(sql,Drinker)
		return items

	def getDrinkerTransactions(self,drinker):
		sql = "SELECT b.bar AS bar, b.date AS date, b.time, b.bill_id AS bill_id,\
				t.item AS item, t.quantity AS quantity, t.price AS price\
				FROM Transactions t, (SELECT *\
				FROM Bills\
				WHERE drinker = \""   + str(drinker) + "\") b \
				WHERE b.bill_id = t.bill_id \
				GROUP BY b.bar, b.date, t.item \
				ORDER BY b.date DESC, b.time DESC; \
				"
		items = self.query(sql,DrinkerTransactionDTO)
		return items

	def getDrinkerTopBeer(self,drinker):
		sql =  "SELECT \
				t.item AS name, SUM(t.quantity) AS amount \
				FROM Transactions t, (SELECT *  \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				WHERE b.bill_id = t.bill_id AND t.type = \""+str("beer")+"\" \
				GROUP BY t.item \
				ORDER BY quantity DESC \
				LIMIT 5; \
				"
		items = self.query(sql,QuantityDTO)
		return items	

	def getDrinkerBarSpending(self,drinker):
		sql =  "SELECT 	b.bar AS name, SUM(b.total_price) AS amount \
				FROM (SELECT * \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY b.bar;"
		items = self.query(sql,QuantityDTO)
		return items	

	def getDrinkerSpendingByDay(self,drinker):
		sql =  "SELECT b.date AS period, SUM(b.total_price) AS amount \
				FROM (SELECT * \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY b.date;"
		items = self.query(sql,PeriodDistributionDTO)
		return items	

	def getDrinkerSpendingByWeek(self,drinker):
		sql = "SELECT week(b.date) AS period, SUM(b.total_price) AS amount \
				FROM (SELECT *\
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY period;"

		items = self.query(sql,PeriodDistributionDTO)
		return items	

	def getDrinkerSpendingByMonth(self,drinker):
		sql = "SELECT monthname(b.date) AS period, SUM(b.total_price) AS amount \
				FROM (SELECT *\
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY period;"

		items = self.query(sql,PeriodDistributionDTO)
		return items

	def insertDrinker(self,drinker):
		sql = "Insert INTO Drinker Values (%s,%s,%s)"
		vals = (drinker.getName(),drinker.getPhone(),drinker.getState())
		return self.insert(sql,vals)


	def updateDrinker(self,drinker):
		sql = "UPDATE Drinker SET name = %s, phone = %s, state = %s WHERE name = %s "
		vals = (drinker.getName(),drinker.getPhone(),drinker.getState(),drinker.getName())
		return self.update(sql,vals)

	def deleteDrinker(self,drinker):
		sql = "DELETE FROM Drinker where name = %s "
		vals = (drinker.getName(),)
		return self.delete(sql,vals)