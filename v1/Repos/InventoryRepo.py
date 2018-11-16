import v1.Repos.SQL as SQL

from v1.Entity.Inventory import Inventory
from datetime import datetime, timedelta

class InventoryRepo(SQL.SQL_table):
	
	def __init__(self):
		super(InventoryRepo, self).__init__()

	def getAllInventory(self):
		sql = "Select * from Inventory ORDER BY bar"
		items = self.query(sql,Inventory)
		return items
	
	def getInventory(self, bar, beer, date):
		sql = "Select * from Inventory WHERE bar = \""+str(bar)+"\" \
				AND beer = \""+str(beer)+"\" AND date >= \""+str(date)+"\" \
				ORDER BY date ASC"
		items = self.query(sql,Inventory)
		return items

	def getInventoryForToday(self, bar, beer, date):
		sql = "Select * from Inventory WHERE bar = \""+str(bar)+"\" \
				AND beer = \""+str(beer)+"\" AND date = \""+str(date)+"\""
		items = self.query(sql,Inventory)
		return items

	def insertInventory(self,inventory):
		sql = "INSERT INTO Inventory (bar, beer, date, startquantity, endquantity) VALUES (%s,%s,%s,%s,%s)"
		vals = (inventory.getBar(),inventory.getBeer(),inventory.getDate(),inventory.getStartQuantity(),inventory.getEndQuantity())
		return self.insert(sql,vals)

	def updateInventory(self,inventory,oldDate, oldBar, oldBeer):
		sql = "UPDATE Inventory SET bar = %s, beer = %s, date = %s, startquantity = %s, endquantity = %s WHERE bar = %s and date = %s and beer= %s "
		vals = (inventory.getBar(), inventory.getBeer(), inventory.getDate(), inventory.getStartQuantity(), inventory.getEndQuantity(), oldBar, oldDate, oldBeer)
		return self.update(sql,vals)

	def deleteInventory(self,inventory):
		sql = "DELETE FROM Inventory WHERE bar = %s and date = %s and beer= %s "
		vals = (inventory.getBar(), inventory.getBeer(), inventory.getDate())
		return self.delete(sql,vals)

	def getAllInventoryFromYesterday(self):
		num = 1
		date_N_days_ago = datetime.now() - timedelta(days=num)
		sql = "select * from Inventory where date = \"" + str(str(date_N_days_ago).split()[0]) + "\"; "
		items = self.query(sql,Inventory)
		return items

	# def insertInventoryForToday(self,listOfPrevousDayObjects):
	# 	num = 1	
	# 	for item in listOfPrevousDayObjects:
	# 		inventory = Inventory()
	# 		inventory.setBeer(item.getBeer())
	# 		inventory.setBar(item.getBar())
	# 		date_N_days_ago = datetime.now() - timedelta(days=num-1)
	# 		inventory.setDate(str(str(date_N_days_ago).split()[0]))
	# 		inventory.setStartQuantity(item.getEndQuantity())
	# 		inventory.setEndQuantity(item.getEndQuantity())

	# 		sql = "INSERT INTO Inventory (bar, beer, date, startquantity, endquantity )VALUES (%s,%s,%s,%s,%s)"
	# 		vals = (inventory.getBar(),inventory.getBeer(),inventory.getDate(),inventory.getStartQuantity(),inventory.getEndQuantity())
		
	# 		#insert new object in to table
	# 		self.insertWithoutClose(sql,vals)
	# 	self.close()

		# return "Success"

	def getLastInsertedDate(self):
		sql = "Select * from Inventory group by date order by date desc"
		items = self.query(sql,Inventory)
		return items[0].getDate()


	def getLastInvetory(self,date):
		sql = "Select * from Inventory where date = \"" + str(date) + "\""
		items = self.query(sql,Inventory)
		return items

	def insertInventoryForToday(self,inventory):
		sql = "INSERT INTO Inventory (bar, beer, date, startquantity, endquantity )VALUES (%s,%s,%s,%s,%s)"
		vals = (inventory.getBar(),inventory.getBeer(),inventory.getDate(),inventory.getStartQuantity(),inventory.getEndQuantity())
		return self.insert(sql,vals)
		


