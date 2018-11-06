import v1.Repos.SQL as SQL

from v1.Entity.SellsFood import SellsFood

class SellsFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(SellsFoodRepo, self).__init__()

	def getAllSellsFood(self):
		sql = "Select * from SellsFood"
		items = self.query(sql,SellsFood)
		return items
