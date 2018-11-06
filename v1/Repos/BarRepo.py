import v1.Repos.SQL as SQL

from v1.DTO.QuantityDTO import QuantityDTO
from v1.Entity.Bar import Bar

from v1.DTO.DistributionDTO import DistributionDTO


class BarRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BarRepo, self).__init__()

	def getAllBars(self):
		sql = "Select * from Bar"
		items = self.query(sql,Bar)
		return items


	def getbarTopBeerBrand(self,bar,dayOfWeek):
		sql = "SELECT manf, SUM(quantity) AS quantity \
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
				ORDER BY amount_spent DESC \
				LIMIT 10; "
		items = self.query(sql,QuantityDTO)
		return items


	def getSaleDistributionDays(self,bar):
		sql = "SELECT b.day AS period, COUNT(b.bill_id) AS num_bills \
				FROM (SELECT * \
				FROM Bills \
				WHERE bar = \""+str(bar)+"\") b \
				GROUP BY b.day \
				ORDER BY dayofweek(b.date);"
		items = self.query(sql,DistributionDTO)
		return items

