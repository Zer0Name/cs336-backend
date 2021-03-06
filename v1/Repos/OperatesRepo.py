import v1.Repos.SQL as SQL
from datetime import datetime, timedelta
from v1.Entity.Operates import Operates
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class OperatesRepo(SQL.SQL_table):
	
	def __init__(self):
		super(OperatesRepo, self).__init__()

	def getAllOperates(self):
		sql = "Select * from Operates ORDER BY bar"
		items = self.query(sql,Operates)
		return items
	
	def getOperatesForBar(self,bar):
		sql = "SELECT * FROM Operates WHERE bar = \""+str(bar)+"\""
		items = self.query(sql,Operates)
		return items
	
	def insertOperates(self,operates):
		sql = "INSERT INTO Operates (bar, day, start, end, date) VALUES (%s, %s, %s, %s, %s)"
		vals = (operates.getBar(),operates.getDay(), operates.getStart(), operates.getEnd(), operates.getDate())
		return self.insert(sql,vals)


	def updateOperates(self,operates,oldDate, oldBar):
		sql = "UPDATE Operates SET bar = %s, day = %s, start = %s, end = %s, date = %s WHERE bar = %s and date = %s "
		vals = (operates.getBar(),operates.getDay(), operates.getStart(), operates.getEnd(), operates.getDate(), oldBar, oldDate)
		return self.update(sql,vals)

	def deleteOperates(self,operates):
		sql = "DELETE FROM Operates WHERE bar = %s and date = %s "
		vals = (operates.getBar(),operates.getDate())
		return self.delete(sql,vals)

	def updateIncorrectOperates(self):
		sql = "Select * from Operates where day =\"" + str("Monday") + "\" " 
		items = self.query(sql,Operates)
		for item in items:
			item.setDate("2018-10-15")
			sql_q = "UPDATE Operates SET date = %s WHERE bar = %s and day = %s"
			vals = (item.getDate(), item.getBar(),item.getDay())
			# self.update(sql_q,vals)
		self.close()

		
	def getLastInsertedDate(self):
		sql = "Select * from Operates group by date order by date desc"
		items = self.query(sql,Operates)
		return items[0].getDate()


	def getLastOperates(self,date):
		datetime_object = datetime.strptime(date, "%Y-%m-%d")
		datetime_object = datetime_object - timedelta(days=6)
		sql = "Select * from Operates where date = \"" +str(str(datetime_object).split()[0]) + "\""
		items = self.query(sql,Operates)
		return items

	def insertOperatesForToday(self,item):
		sql = "INSERT INTO Operates (bar, day, start, end, date)VALUES (%s,%s,%s,%s,%s)"
		vals = (item.getBar(), item.getDay(), item.getStart(), item.getEnd(), item.getDate() )
		#insert new object in to table
		return self.insert(sql,vals)
	
	#covers pattern 1
	def time_during_operating_hours(self, time, bar, date):
		sql = "SELECT EXISTS(SELECT * FROM Operates WHERE  \
				bar = \""+str(bar)+"\" AND date = \""+str(date)+"\" \
				AND \""+str(time)+"\" >= start AND \""+str(time)+"\" <= end) AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	#checks
	def duplicate_entry(self, bar, date):
		sql = "SELECT EXISTS(SELECT * FROM Operates WHERE bar = \""+str(bar)+"\" \
				 AND date = \""+str(date)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def shift_during_operating_hours(self, start, end, bar, date):
		sql = "SELECT EXISTS(SELECT * FROM Operates WHERE  \
				bar = \""+str(bar)+"\" AND date = \""+str(date)+"\" \
				AND \""+str(start)+"\" >= start AND \""+str(end)+"\" <= end) AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False