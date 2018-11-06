import v1.Repos.SQL as SQL
from v1.DTO.QuantityDTO import QuantityDTO
from v1.DTO.NameDTO import NameDTO

class ManufacturerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(ManufacturerRepo, self).__init__()
	
	def getAllManufacturers(self):
		sql = "SELECT DISTINCT manf AS name FROM Beer"
		items = self.query(sql,NameDTO)
		return items
	
	def getAllBeersByManufacturer(self,manf):
		sql = "SELECT name FROM Beer WHERE manf = \""+str(manf)+"\""
		items = self.query(sql,NameDTO)
		return items

	#need to change dates to current date
	def getTop10StatesWithHighestSalesInTheLastWeek(self,manf):
		sql = "SELECT b1.state AS name, SUM(t.quantity) AS amount \
				FROM (SELECT name AS beer \
				FROM Beer \
				WHERE manf = \""+str(manf)+"\") m, \
				(SELECT bill_id, date, bar \
				FROM Bills \
				WHERE date BETWEEN date_sub(\""+str("2018-10-22")+"\",INTERVAL 1 WEEK) AND '2018-10-22') b, \
				Transactions t, Bar b1 \
				WHERE b.bill_id = t.bill_id AND t.item = m.beer AND b1.name = b.bar \
				GROUP BY b1.state \
				ORDER BY amount DESC \
				LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items
	
	def getTop10StatesWhereTheirBeerIsLikedTheMost(self,manf):
		sql = "SELECT state AS name, COUNT(*) AS amount \
				FROM (SELECT DISTINCT l.drinker \
				FROM (SELECT name AS beer \
				FROM Beer \
				WHERE manf = \""+str(manf)+"\") m, Likes l \
				WHERE l.beer = m.beer) d, Drinker d1 \
				WHERE d.drinker = d1.name \
				GROUP BY state \
				ORDER BY amount desc \
				LIMIT 10;"
		items = self.query(sql,QuantityDTO)
		return items