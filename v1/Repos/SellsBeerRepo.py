import v1.Repos.SQL as SQL

from v1.Entity.SellsBeer import SellsBeer

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

