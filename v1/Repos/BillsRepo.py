import v1.Repos.SQL as SQL

from v1.Entity.Bills import Bills
from v1.Entity.Transactions import Transactions
from v1.DTO.TrueFalseDTO import TrueFalseDTO

class BillsRepo(SQL.SQL_table):
	
	def __init__(self):
		super(BillsRepo, self).__init__()

	def getAllBills(self):
		sql = "Select * from Bills"
		items = self.query(sql,Bills)
		return items

	def insertBills(self,bills):
		sql = "INSERT INTO Bills (bill_id, bar, drinker, date, items_price, tax_price, tip, total_price, time, bartender, day) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		vals = (bills.getBillId(), bills.getBar(), bills.getDrinker(), bills.getDate(),bills.getItemsPrice(), bills.getTax(), bills.getTip(), bills.getTotalPrice(), bills.getTime(), bills.getBartender(), bills.getDay())
		return self.insert(sql,vals)

	def updateBills(self,bills,oldBillId):
		sql = "UPDATE Bills SET bill_id = %s, bar = %s, drinker = %s, date = %s, items_price = %s, tax_price = %s, tip = %s, total_price = %s, time = %s, bartender = %s, day = %s  WHERE bill_id = %s "
		vals = (bills.getBillId(), bills.getBar(), bills.getItem(), bills.getQuantity(), bills.getDrinker(), bills.getDate(),bills.getType(), bills.getPrice(), oldBillId)
		return self.update(sql,vals)

	def deleteBills(self,bills):
		sql = "DELETE FROM Bills WHERE bill_id = %s "
		vals = (bills.getBillId())
		return self.delete(sql,vals)

	#checks for insert and update
	
	def duplicate_entry(self, bill_id):
		sql = "SELECT EXISTS(SELECT * FROM Bills WHERE bill_id = \""+str(bill_id)+"\") AS value"
		items = self.query(sql,TrueFalseDTO)
		if int(items[0].value) == 1:
			return True
		return False
	
	def check_items_price(self, bill_id, items_price):
		sql = "SELECT * FROM Transactions WHERE bill_id = \""+str(bill_id)+"\""
		items = self.query(sql,Transactions)
		count = 0.00
		for t in items:
			count = count + t.getPrice()
		if float(count) == float(items_price):
			return True
		return False
	