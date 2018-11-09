import v1.Repos.SQL as SQL

from v1.Entity.Transactions import Transactions

class TransactionsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(TransactionsRepo, self).__init__()

	def getAllTransactions(self):
		sql = "Select * from Transactions"
		items = self.query(sql,Transactions)
		return items

	#need to delete bar, drinker, and date once update transactions
	def insertTransactions(self,transactions):
		sql = "INSERT INTO Transactions (bill_id, bar, item, quantity, drinker, date, type, price) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
		vals = (transactions.getBillId(), transactions.getBar(), transactions.getItem(), transactions.getQuantity(), transactions.getDrinker(), transactions.getDate(),transactions.getType(), transactions.getPrice())
		return self.insert(sql,vals)

	#need to delete bar, drinker, and date once update transactions
	def updateTransactions(self,transactions,oldBillId,oldItem):
		sql = "UPDATE Transactions SET bill_id = %s, bar = %s, item = %s, quantity = %s, drinker = %s, date = %s, type = %s, price = %s WHERE bill_id = %s and item = %s "
		vals = (transactions.getBillId(), transactions.getBar(), transactions.getItem(), transactions.getQuantity(), transactions.getDrinker(), transactions.getDate(),transactions.getType(), transactions.getPrice(), oldBillId, oldItem)
		return self.update(sql,vals)

	def deleteTransactions(self,transactions):
		sql = "DELETE FROM Transactions WHERE bill_id = %s and item = %s "
		vals = (transactions.getBillId(), transactions.getItem())
		return self.delete(sql,vals)
