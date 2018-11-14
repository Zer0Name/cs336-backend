import v1.Repos.SQL as SQL

from v1.Entity.SellsFood import SellsFood
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class SellsFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(SellsFoodRepo, self).__init__()

	def getAllSellsFood(self):
		sql = "Select * from SellsFood"
		items = self.query(sql,SellsFood)
		return items
	
	def insertSellsFood(self,sellsFood):
		sql = "INSERT INTO SellsFood (foodname, barname, price) VALUES (%s, %s, %s)"
		vals = (sellsFood.getFoodname(),sellsFood.getBarname(), sellsFood.getPrice())
		return self.insert(sql,vals)


	def updateSellsFood(self,sellsFood,oldFood, oldBar):
		sql = "UPDATE SellsFood SET foodname = %s, barname = %s, price = %s WHERE foodname = %s and barname = %s "
		vals = (sellsFood.getFoodname(),sellsFood.getBarname(), sellsFood.getPrice(), oldFood, oldBar)
		return self.update(sql,vals)

	def deleteSellsFood(self,sellsFood):
		sql = "DELETE FROM SellsFood WHERE foodname = %s and barname = %s "
		vals = (sellsFood.getFoodname(),sellsFood.getBarname())
		return self.delete(sql,vals)
	
	def bar_sells_food(self, bar, food):
		sql = "SELECT EXISTS(SELECT * FROM SellsFood WHERE barname = \""+str(bar)+"\" \
				AND  foodname = \""+str(food)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def get_price(self, bar, food):
		sql = "SELECT price AS value FROM SellsFood WHERE barname = \""+str(bar)+"\" \
				AND  beername = \""+str(food)+"\""
		items = self.query(sql,TrueFalseDTO)
		return int(items[0].value)

	def duplicate_entry(self, food, bar):
		sql = "SELECT EXISTS(SELECT * FROM SellsFood WHERE foodname = \""+str(food)+"\" \
					AND barname = \""+str(bar)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
