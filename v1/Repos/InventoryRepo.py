import v1.Repos.SQL as SQL

from v1.Entity.Inventory import Inventory

class InventoryRepo(SQL.SQL_table):
	
	def __init__(self):
		super(InventoryRepo, self).__init__()

	def getAllInventory(self):
		sql = "Select * from Inventory"
		items = self.query(sql,Inventory)
		return items
