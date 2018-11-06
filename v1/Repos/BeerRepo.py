import v1.Repos.SQL as SQL
from v1.Entity.Beer import Beer



from v1.DTO.QuantityDTO import QuantityDTO

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
		sql = "SELECT drinker as name, SUM(quantity) AS amount\
				FROM Transactions \
				WHERE item = \""+str(beer)+"\" \
				GROUP BY drinker \
				ORDER BY amount DESC \
				LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items
