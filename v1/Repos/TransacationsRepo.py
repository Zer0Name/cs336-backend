import v1.Repos.SQL as SQL

from v1.Entity.Transactions import Transactions

class TransactionsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(TransactionsRepo, self).__init__()

	def getAllTransactions(self):
		sql = "Select * from Transactions"
		items = self.query(sql,Transactions)
		return items
