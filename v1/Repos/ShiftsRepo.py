import v1.Repos.SQL as SQL

from v1.Entity.Shifts import Shifts

class ShiftsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(ShiftsRepo, self).__init__()

	def getAllShifts(self):
		sql = "Select * from Shifts"
		items = self.query(sql,Shifts)
		return items
