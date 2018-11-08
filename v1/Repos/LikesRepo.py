import v1.Repos.SQL as SQL

from v1.Entity.Likes import Likes

class LikesRepo(SQL.SQL_table):
	
	def __init__(self):
		super(LikesRepo, self).__init__()

	def getAllLikes(self):
		sql = "Select * from Likes"
		items = self.query(sql,Likes)
		return items
	
	def insertLikes(self,likes):
		sql = "INSERT INTO Likes (drinker, beer) VALUES (%s, %s)"
		vals = (likes.getDrinker(),likes.getBeer())
		return self.insert(sql,vals)


	def updateLikes(self,likes,oldDrinker, oldBeer):
		sql = "UPDATE Likes SET drinker = %s, beer = %s WHERE drinker = %s and beer = %s "
		vals = (likes.getDrinker(),likes.getBeer(), oldDrinker, oldBeer)
		return self.update(sql,vals)

	def deleteLikes(self,likes):
		sql = "DELETE FROM Likes WHERE drinker = %s and beer = %s "
		vals = (likes.getDrinker(),likes.getBeer())
		return self.delete(sql,vals)


