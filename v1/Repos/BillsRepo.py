import v1.Repos.SQL as SQL

from v1.Entity.Bills import Bills

class BillsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BillsRepo, self).__init__()

	def getAllBills(self):
		sql = "Select * from Bills"
		items = self.query(sql,Bills)
		return items
