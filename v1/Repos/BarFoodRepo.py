import v1.Repos.SQL as SQL

from v1.Entity.BarFood import BarFood

class BarFoodRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BarFoodRepo, self).__init__()

	def getAllBarFood(self):
		sql = "Select * from BarFood"
		items = self.query(sql,BarFood)
		return items

	def insertBarFood(self,BarFood):
		sql = "INSERT INTO BarFood VALUES (%s)"
		vals = (BarFood.getName(),)
		return self.insert(sql,vals)


	def updateBarFood(self,BarFood,oldName):
		sql = "UPDATE BarFood SET name = %s WHERE name = %s "
		vals = (BarFood.getName(),oldName)
		return self.update(sql,vals)

	def deleteBarFood(self,BarFood):
		sql = "DELETE FROM BarFood WHERE name = %s "
		vals = (BarFood.getName(),)
		return self.delete(sql,vals)