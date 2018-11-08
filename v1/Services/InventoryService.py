import v1.Repos.InventoryRepo as InventoryRepo


def insertInventoryForToday():
    inventoryRepo = InventoryRepo.InventoryRepo()
    items  = inventoryRepo.getAllInventoryFromYesterday()
    inventoryRepo = InventoryRepo.InventoryRepo()
    inventoryRepo.insertInventoryForToday(items)
    return "success"

'''
checks to make:
no duplicate entries
bar exists
date exists - can't be past current date
beer exists
startquantity >= endquantity
the bar sells that beer
'''
def insertInventory(inventory):
	inventoryRepo = InventoryRepo.InventoryRepo()
	return inventoryRepo.insertInventory(inventory)

'''
checks to make:
no duplicate entries
bar exists
date exists - can't be past current date
beer exists
startquantity >= endquantity
the bar sells that beer
if updating past inventory have issue with transactions and thus bills
'''
def updateInventory(inventory,oldDate, oldBar, oldBeer):
	inventoryRepo = InventoryRepo.InventoryRepo()
	return inventoryRepo.updateInventory(inventory, oldDate, oldBar, oldBeer)

''' 
checks:

'''
def deleteInventory(inventory):
	inventoryRepo = InventoryRepo.InventoryRepo()
	return inventoryRepo.deleteInventory(inventory)