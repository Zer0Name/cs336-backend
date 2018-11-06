import v1.Repos.SQL as SQL

from v1.Entity.Day import Day

class DayRepo(SQL.SQL_table):
	
	def __init__(self):
		super(DayRepo, self).__init__()

	def getAllDay(self):
		sql = "Select * from Day"
		items = self.query(sql,Day)
		return items
