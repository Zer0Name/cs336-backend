import v1.Repos.SQL as SQL

from v1.Entity.SellsBeer import SellsBeer

class SellsBeerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(SellsBeerRepo, self).__init__()

	def getAllSellsBeer(self):
		sql = "Select * from SellsBeer"
		items = self.query(sql,SellsBeer)
		return items
