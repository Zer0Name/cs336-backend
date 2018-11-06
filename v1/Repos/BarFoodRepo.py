import v1.Repos.SQL as SQL

from v1.Entity.BarFood import BarFood

class BarFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BarFoodRepo, self).__init__()

	def getAllBarFood(self):
		sql = "Select * from BarFood"
		items = self.query(sql,BarFood)
		return items
