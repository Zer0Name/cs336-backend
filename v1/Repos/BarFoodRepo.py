import v1.Repos.SQL as SQL

from v1.Entity.BarFood import BarFood

class BarFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BarFoodRepo, self).__init__()

	def getAllBarFood(self):
		sql = "Select * from BarFood"
		items = self.query(sql,BarFood)
		return items

	def insertBarFood(self,barFood):
		sql = "INSERT INTO BarFood (name) VALUES (%s)"
		vals = (barFood.getName(),)
		return self.insert(sql,vals)


	def updateBarFood(self,barFood,oldName):
		sql = "UPDATE BarFood SET name = %s WHERE name = %s "
		vals = (barFood.getName(),oldName)
		return self.update(sql,vals)

	def deleteBarFood(self,barFood):
		sql = "DELETE FROM BarFood WHERE name = %s "
		vals = (barFood.getName(),)
		return self.delete(sql,vals)