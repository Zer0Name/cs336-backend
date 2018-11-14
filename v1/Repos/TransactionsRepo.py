import v1.Repos.SQL as SQL

from v1.Entity.Transactions import Transactions
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class TransactionsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(TransactionsRepo, self).__init__()

	def getAllTransactions(self):
		sql = "Select * from Transactions ORDER BY bill_id"
		items = self.query(sql,Transactions)
		return items
	
	def getAllTransactionsForBillId(self, bill_id):
		sql = "Select * from Transactions where bill_id = \""+str(bill_id)+"\""
		items = self.query(sql,Transactions)
		return items

	def insertTransactions(self,transactions):
		sql = "INSERT INTO Transactions (bill_id, item, quantity, type, price) VALUES (%s,%s,%s,%s,%s)"
		vals = (transactions.getBillId(), transactions.getItem(), transactions.getQuantity(),transactions.getType(), transactions.getPrice())
		return self.insert(sql,vals)
		
	def updateTransactions(self,transactions,oldBillId,oldItem):
		sql = "UPDATE Transactions SET bill_id = %s, item = %s, quantity = %s, type = %s, price = %s WHERE bill_id = %s and item = %s "
		vals = (transactions.getBillId(), transactions.getItem(), transactions.getQuantity(), transactions.getType(), transactions.getPrice(), oldBillId, oldItem)
		return self.update(sql,vals)

	def deleteTransactions(self,transactions):
		sql = "DELETE FROM Transactions WHERE bill_id = %s and item = %s "
		vals = (transactions.getBillId(), transactions.getItem())
		return self.delete(sql,vals)
	
	#checks
	def duplicate_entry(self, bill_id, item):
		sql = "SELECT EXISTS(SELECT * FROM Transactions WHERE bill_id = \""+str(bill_id)+"\" \
				 AND item = \""+str(item)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def get_quantity(self, bill_id, item):
		sql = "SELECT quantity AS value FROM Transactions WHERE bill_id = \""+str(bill_id)+"\" \
				 AND item = \""+str(item)+"\""
		items = self.query(sql,TrueFalseDTO)
		return int(items[0].value)
	
	def get_items_price(self, bill_id, item):
		sql = "SELECT items_price AS value FROM Transactions WHERE bill_id = \""+str(bill_id)+"\" \
				 AND item = \""+str(item)+"\""
		items = self.query(sql,TrueFalseDTO)
		return float(items[0].value)
