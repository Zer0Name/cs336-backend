import v1.Repos.SQL as SQL

from v1.Entity.Operates import Operates

class OperatesRepo(SQL.SQL_table):
	
	def __init__(self):
		super(OperatesRepo, self).__init__()

	def getAllOperates(self):
		sql = "Select * from Operates"
		items = self.query(sql,Operates)
		return items
	
	def getOperatesForBar(self,bar):
		sql = "SELECT * FROM Operates WHERE bar = \""+str(bar)+"\""
		items = self.query(sql,Operates)
		return items
	
	def insertOperates(self,operates):
		sql = "INSERT INTO Operates (bar, day, start, end) VALUES (%s, %s, %s, %s)"
		vals = (operates.getBar(),operates.getDay(), operates.getStart(), operates.getEnd())
		return self.insert(sql,vals)


	def updateOperates(self,operates,oldDay, oldBar):
		sql = "UPDATE Operates SET bar = %s, day = %s, start = %s, end = %s WHERE bar = %s and day = %s "
		vals = (operates.getBar(),operates.getDay(), operates.getStart(), operates.getEnd(), oldDay, oldBar)
		return self.update(sql,vals)

	def deleteOperates(self,operates):
		sql = "DELETE FROM Operates WHERE bar = %s and day = %s "
		vals = (operates.getBar(),operates.getDay())
		return self.delete(sql,vals)