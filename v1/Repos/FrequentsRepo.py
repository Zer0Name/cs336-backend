import v1.Repos.SQL as SQL

from v1.Entity.Frequents import Frequents

class FrequentsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(FrequentsRepo, self).__init__()

	def getAllFrequents(self):
		sql = "Select * from Frequents"
		items = self.query(sql,Frequents)
		return items
