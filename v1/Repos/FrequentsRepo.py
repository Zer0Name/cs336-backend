import v1.Repos.SQL as SQL

from v1.Entity.Frequents import Frequents

class FrequentsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(FrequentsRepo, self).__init__()

	def getAllFrequents(self):
		sql = "Select * from Frequents"
		items = self.query(sql,Frequents)
		return items
	
	def insertFrequents(self,frequents):
		sql = "INSERT INTO Frequents (drinker, bar) VALUES (%s, %s)"
		vals = (frequents.getDrinker(),frequents.getBar())
		return self.insert(sql,vals)


	def updateFrequents(self,frequents,oldDrinker, oldBar):
		sql = "UPDATE Frequents SET drinker = %s, bar = %s WHERE drinker = %s and bar = %s "
		vals = (frequents.getDrinker(),frequents.getBar(), oldDrinker, oldBar)
		return self.update(sql,vals)

	def deleteFrequents(self,frequents):
		sql = "DELETE FROM Frequents WHERE drinker = %s and bar = %s "
		vals = (frequents.getDrinker(),frequents.getBar())
		return self.delete(sql,vals)

