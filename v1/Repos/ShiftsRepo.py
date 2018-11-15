import v1.Repos.SQL as SQL

from v1.Entity.Shifts import Shifts
from datetime import datetime, timedelta
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class ShiftsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(ShiftsRepo, self).__init__()

	def getAllShifts(self):
		sql = "Select * from Shifts ORDER BY bartender"
		items = self.query(sql,Shifts)
		return items

	def getShifts(self,bartender,date):
		sql = "Select * from Shifts where bartender = \"" + str(bartender) + "\" and date = \"" + str(date) + "\" " 
		items = self.query(sql,Shifts)
		return items

	def getShiftsForBar(self,bar,date):
		sql = "Select * from Shifts where bar = \"" + str(bar) + "\" and date = \"" + str(date) + "\" " 
		items = self.query(sql,Shifts)
		return items

	def getBartenderpreviousShift(self,bartender):
		date_N_days_ago = datetime.now() - timedelta(days=7)
		
		sql = "Select * from Shifts where name = \"" + bartender.getName() + "\" and date = \"" +str(str(date_N_days_ago).split()[0]) + "\""
		items = self.query(sql,Shifts)
		for item in items:
			print item

	def getLastInsertedDate(self):
		sql = "Select * from Shifts group by date order by date desc"
		items = self.query(sql,Shifts)
		return items[0].getDate()


	def getLastShifts(self,date):
		datetime_object = datetime.strptime(date, "%Y-%m-%d")
		datetime_object = datetime_object - timedelta(days=6)
		sql = "Select * from Shifts where date = \"" +str(str(datetime_object).split()[0]) + "\""
		items = self.query(sql,Shifts)
		return items

	def insertShiftsForToday(self,item):
		sql = "INSERT INTO Shifts (bar, bartender,day, start, end, date )VALUES (%s,%s,%s,%s,%s,%s)"
		vals = (item.getBar(),item.getBartender(),item.getDay(),item.getStart(),item.getEnd(),item.getDate())
		return self.insert(sql,vals)
		

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


	def insertShifts(self,shifts):
		sql = "INSERT INTO Shifts (bar, bartender, day, start, end, date) VALUES (%s,%s,%s,%s,%s,%s)"
		vals = (shifts.getBar(), shifts.getBartender(), shifts.getDay(),shifts.getStart(), shifts.getEnd(), shifts.getDate())
		return self.insert(sql,vals)

	def updateShifts(self,shifts,oldBar, oldBartender, oldDate):
		sql = "UPDATE Shifts SET bar = %s, bartender = %s, day = %s, start = %s, end = %s, date = %s  WHERE bar = %s and bartender = %s and date = %s "
		vals = (shifts.getBar(), shifts.getBartender(), shifts.getDay(), shifts.getStart(), shifts.getEnd(),shifts.getDay(), oldBar, oldBartender, oldDate)
		return self.update(sql,vals)

	def deleteShifts(self,shifts):
		sql = "DELETE FROM Shifts WHERE bar = %s and bartender = %s  and date = %s "
		vals = (shifts.getBar(), shifts.getBartender(), shifts.getDate())
		return self.delete(sql,vals)	
	
	def time_during_shift(self, time, bartender, bar, date):
		sql = "SELECT EXISTS(SELECT * FROM Shifts WHERE bartender = \""+str(bartender)+"\" \
				AND bar = \""+str(bar)+"\" AND date = \""+str(date)+"\" \
				AND \""+str(time)+"\" >= start AND \""+str(time)+"\" <= end) AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def shift_at_time(self, time, bar, date):
		sql = "SELECT EXISTS(SELECT * FROM Shifts WHERE \
				bar = \""+str(bar)+"\" AND date = \""+str(date)+"\" \
				AND \""+str(time)+"\" >= start AND \""+str(time)+"\" <= end) AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False