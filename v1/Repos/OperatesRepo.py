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
