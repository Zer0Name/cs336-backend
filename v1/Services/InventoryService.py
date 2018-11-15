from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.InventoryRepo as InventoryRepo
from datetime import datetime, timedelta

def getAllInventory(num):
	inventoryRepo = InventoryRepo.InventoryRepo() 
	results = inventoryRepo.getAllInventory()
	if len(results) <= num:
		return jsonify([])
	if num+5000 >= len(results):
		return  jsonify([e.toJson() for e in results[num:]])
	else:
		return  jsonify([e.toJson() for e in results[num: num+5000]])

def insertInventoryForToday():

	inventoryRepo = InventoryRepo.InventoryRepo()
	date =  str(inventoryRepo.getLastInsertedDate())
	date_N_days_ago = datetime.now()
	if str(str(date_N_days_ago).split()[0]) == str(date):
		return "day already inserted"

	inventoryRepo = InventoryRepo.InventoryRepo()
	items = inventoryRepo.getLastInvetory(date)

	for item in items:
		item.setDate(str(str(date_N_days_ago).split()[0]))
		try:
			inventoryRepo = InventoryRepo.InventoryRepo()
			inventoryRepo.insertInventoryForToday(item)
		except:
			pass
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