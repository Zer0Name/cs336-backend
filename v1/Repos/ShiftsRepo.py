import v1.Repos.SQL as SQL

from v1.Entity.Shifts import Shifts
from datetime import datetime, timedelta

class ShiftsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(ShiftsRepo, self).__init__()

	def getAllShifts(self):
		sql = "Select * from Shifts"
		items = self.query(sql,Shifts)
		return items

	def getBartenderpreviousShift(self,bartender):
		date_N_days_ago = datetime.now() - timedelta(days=7)
		
		sql = "Select * from Shifts where name = \"" + bartender.getName() + "\" and date = \"" +str(str(date_N_days_ago).split()[0]) + "\""
		items = self.query(sql,Shifts)
		for item in items:
			print item

	

	def updateSHIFT(self):
		# date_N_days_ago = datetime.now() - timedelta(days=30)
		# print date_N_days_ago
		
		sql = "Select * from Shifts where day =\"" + str("Monday") + "\" " 
		items = self.query(sql,Shifts)
		for item in items:
			item.setDate("2018-10-15")
			sql_q = "UPDATE Shifts SET date = %s WHERE bar = %s and  bartender = %s and day = %s"
			vals = (item.getDate(), item.getBar(), item.getBartender(), item.getDay())
			self.update(sql_q,vals)
		self.close()



			