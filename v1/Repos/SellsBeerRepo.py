import v1.Repos.SQL as SQL

from v1.Entity.SellsBeer import SellsBeer
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class SellsBeerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(SellsBeerRepo, self).__init__()

	def getAllSellsBeer(self):
		sql = "Select * from SellsBeer"
		items = self.query(sql,SellsBeer)
		return items
	
	def insertSellsBeer(self,sellsBeer):
		sql = "INSERT INTO SellsBeer (beername, barname, price) VALUES (%s, %s, %s)"
		vals = (sellsBeer.getBeer(),sellsBeer.getBar(), sellsBeer.getPrice())
		return self.insert(sql,vals)


	def updateSellsBeer(self,sellsBeer,oldBeer, oldBar):
		sql = "UPDATE SellsBeer SET beername = %s, barname = %s, price = %s WHERE beername = %s and barname = %s "
		vals = (sellsBeer.getBeer(),sellsBeer.getBar(), sellsBeer.getPrice(), oldBeer, oldBar)
		return self.update(sql,vals)

	def deleteSellsBeer(self,sellsBeer):
		sql = "DELETE FROM SellsBeer WHERE beername = %s and barname = %s "
		vals = (sellsBeer.getBeer(),sellsBeer.getBar())
		return self.delete(sql,vals)
	
	def bar_sells_beer(self, bar, beer):
		sql = "SELECT EXISTS(SELECT * FROM SellsBeer WHERE barname = \""+str(bar)+"\" \
				AND  beername = \""+str(beer)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def get_price(self, bar, beer):
		sql = "SELECT price AS value FROM SellsBeer WHERE barname = \""+str(bar)+"\" \
				AND  beername = \""+str(beer)+"\""
		items = self.query(sql,TrueFalseDTO)
		return int(items[0].value)
	
	def duplicate_entry(self, beer, bar):
		sql = "SELECT EXISTS(SELECT * FROM SellsBeer WHERE beername = \""+str(beer)+"\" \
					AND barname = \""+str(bar)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False

