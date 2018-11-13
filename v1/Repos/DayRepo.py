import v1.Repos.SQL as SQL

from v1.Entity.Day import Day
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class DayRepo(SQL.SQL_table):
	
	def __init__(self):
		super(DayRepo, self).__init__()

	def getAllDay(self):
		sql = "Select * from Day"
		items = self.query(sql,Day)
		return items
	
	def insertDay(self,day):
		sql = "INSERT INTO Day (name) VALUES (%s)"
		vals = (day.getName(),)
		return self.insert(sql,vals)


	def updateDay(self,day,oldName):
		sql = "UPDATE Day SET name = %s WHERE name = %s "
		vals = (day.getName(),oldName)
		return self.update(sql,vals)

	def deleteDay(self,day):
		sql = "DELETE FROM Day WHERE name = %s "
		vals = (day.getName(),)
		return self.delete(sql,vals)
	
	def day_exists(self, day):
		sql = "SELECT EXISTS(SELECT * FROM Day WHERE name = \""+str(day)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False

