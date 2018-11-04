import v1.Repos.SQL as SQL
from v1.Entity.Beer import Beer

class BeerRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BeerRepo, self).__init__()
	
	def getAllBeers(self):
		sql = "Select * from Beer"
		items = self.query(sql)
		result = []
		for item in items:
			beer = Beer()
			beer.map(item)
			result.append(beer)
		self.close()
		return result
