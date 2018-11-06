import v1.Repos.SQL as SQL

from v1.Entity.Likes import Likes

class LikesRepo(SQL.SQL_table):
	
	def __init__(self):
		super(LikesRepo, self).__init__()

	def getAllLikes(self):
		sql = "Select * from Likes"
		items = self.query(sql,Likes)
		return items
