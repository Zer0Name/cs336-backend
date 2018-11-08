import v1.Repos.SQL as SQL

from v1.Entity.SellsFood import SellsFood

class SellsFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(SellsFoodRepo, self).__init__()

	def getAllSellsFood(self):
		sql = "Select * from SellsFood"
		items = self.query(sql,SellsFood)
		return items
	
	def insertSellsFood(self,sellsFood):
		sql = "INSERT INTO SellsFood (foodname, barname, price) VALUES (%s, %s, %s)"
		vals = (sellsFood.getFood(),sellsFood.getBar(), sellsFood.getPrice())
		return self.insert(sql,vals)


	def updateSellsFood(self,sellsFood,oldFood, oldBar):
		sql = "UPDATE SellsFood SET foodname = %s, barname = %s, price = %s WHERE foodname = %s and barname = %s "
		vals = (sellsFood.getFood(),sellsFood.getBar(), sellsFood.getPrice(), oldFood, oldBar)
		return self.update(sql,vals)

	def deleteSellsFood(self,sellsFood):
		sql = "DELETE FROM SellsFood WHERE foodname = %s and barname = %s "
		vals = (sellsFood.getFood(),sellsFood.getBar())
		return self.delete(sql,vals)
