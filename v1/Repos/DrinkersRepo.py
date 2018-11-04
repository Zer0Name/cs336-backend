import v1.Repos.SQL as SQL
from v1.Entity.Drinker import Drinker
from v1.DTO.DrinkerTransactionDTO import DrinkerTransactionDTO
from v1.DTO.DrinkerTopBeerDTO import DrinkerTopBeerDTO
from v1.DTO.SpendingDTO import SpendingDTO
from v1.DTO.DrinkerSpendingByTimeDTO import DrinkerSpendingByTimeDTO

class DrinkerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(DrinkerRepo, self).__init__()

	def getAllDrinkers(self):
		sql = "Select * from Drinker"
		items = self.query(sql)
		result = []
		for item in items:
			drinker = Drinker()
			drinker.map(item)
			result.append(drinker)
		self.close()
		return result

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
		items = self.query(sql)
		result = []
		for item in items:
			drinkerTransactionDTO = DrinkerTransactionDTO()
			drinkerTransactionDTO.map(item)
			result.append(drinkerTransactionDTO)
		self.close()
		return result

	def getDrinkerTopBeer(self,drinker):
		sql =  "SELECT \
				t.item AS beer, SUM(t.quantity) AS quantity \
				FROM Transactions t, (SELECT *  \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				WHERE b.bill_id = t.bill_id AND t.type = \""+str("beer")+"\" \
				GROUP BY t.item \
				ORDER BY quantity DESC \
				LIMIT 5; \
				"
		items = self.query(sql)
		result = []
		for item in items:
			drinkerTopBeerDTO = DrinkerTopBeerDTO()
			drinkerTopBeerDTO.map(item)
			result.append(drinkerTopBeerDTO)
		self.close()
		return result	

	def getDrinkerBarSpending(self,drinker):
		sql =  "SELECT 	b.bar AS name, SUM(b.total_price) AS amount_spent \
				FROM (SELECT * \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY b.bar;"
		items = self.query(sql)
		result = []
		for item in items:
			spendingDTO = SpendingDTO()
			spendingDTO.map(item)
			result.append(spendingDTO)
		self.close()
		return result	

	def getDrinkerSpendingByDay(self,drinker):
		sql =  "SELECT b.date AS period, SUM(b.total_price) AS amount_spent \
				FROM (SELECT * \
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY b.date;"
		items = self.query(sql)
		result = []
		for item in items:
			drinkerSpendingByTimeDTO = DrinkerSpendingByTimeDTO()
			drinkerSpendingByTimeDTO.map(item)
			result.append(drinkerSpendingByTimeDTO)
		self.close()
		return result	

	def getDrinkerSpendingByWeek(self,drinker):
		sql = "SELECT week(b.date) AS period, SUM(b.total_price) AS amount_spent \
				FROM (SELECT *\
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY period;"

		items = self.query(sql)
		result = []
		for item in items:
			drinkerSpendingByTimeDTO = DrinkerSpendingByTimeDTO()
			drinkerSpendingByTimeDTO.map(item)
			result.append(drinkerSpendingByTimeDTO)
		self.close()
		return result	

	def getDrinkerSpendingByMonth(self,drinker):
		sql = "SELECT monthname(b.date) AS period, SUM(b.total_price) AS amount_spent \
				FROM (SELECT *\
				FROM Bills \
				WHERE drinker = \""+str(drinker)+"\") b \
				GROUP BY period;"

		items = self.query(sql)
		result = []
		for item in items:
			drinkerSpendingByTimeDTO = DrinkerSpendingByTimeDTO()
			drinkerSpendingByTimeDTO.map(item)
			result.append(drinkerSpendingByTimeDTO)
		self.close()
		return result	