from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.TransactionsRepo as TransactionsRepo
import v1.Repos.BarFoodRepo as BarFoodRepo
import v1.Repos.SellsBeerRepo as SellsBeerRepo
import v1.Repos.SellsFoodRepo as SellsFoodRepo
import v1.Repos.BillsRepo as BillsRepo
import v1.Repos.BeerRepo as BeerRepo
from v1.Exceptions.Error import Error
import v1.Services.BillsService as billsService
import v1.Repos.InventoryRepo as InventoryRepo
import v1.Services.InventoryService as inventoryService

def getAllTransactions(num):
	transactionsRepo = TransactionsRepo.TransactionsRepo() 
	results = transactionsRepo.getAllTransactions()
   	if len(results) <= num:
		return jsonify([])
	if num+5000 >= len(results):
		return  jsonify([e.toJson() for e in results[num:]])
	else:
		return  jsonify([e.toJson() for e in results[num: num+5000]])

'''
checks to make:
no duplicate entries
if item with that bill_id already exists should add to
that quantity instead of inserting (this may not be necessary)
but either way need to update Bill
quantity can't be 0 or less
item exists - can be food or beer
make sure type is food or beer
the bar sells the item
make sure price is the price the bar sells the item at times the quantity
'''
def insertTransactions(transactions):
	if int(transactions.getQuantity()) <= 0:
		raise Error("Invalid Quantity")

	billsRepo = BillsRepo.BillsRepo()
	bill = billsRepo.getBillArray(transactions.getBillId())
	if len(bill) == 0:
		raise Error("No bill has been created for this transaction. Please insert a bill and try again.")
	bill = bill[0]

	transactionsRepo = TransactionsRepo.TransactionsRepo()
	if transactionsRepo.duplicate_entry(transactions.getBillId(), transactions.getItem()):
		raise Error("item is already a transactions for the current bill please use update to change amount of the item")

	if transactions.getType() == "food":
		barFoodRepo = BarFoodRepo.BarFoodRepo()
		if not barFoodRepo.barFood_exists(transactions.getItem()):
			raise Error("Food does not exist")

		sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
		if not sellsFoodRepo.bar_sells_food(bill.getBar(),transactions.getItem()):
			raise Error("Bar doesn't sell the food")

		sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
		price = sellsFoodRepo.get_price(bill.getBar(), transactions.getItem())

		
	if transactions.getType() == "beer":
		
		beerRepo = BeerRepo.BeerRepo()
		if not beerRepo.beer_exists(transactions.getItem()):
			raise Error("Beer does not exist")

		sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
		if not sellsBeerRepo.bar_sells_beer(bill.getBar(),transactions.getItem()):
			raise Error("Bar doesn't sell the beer")

		sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
		price = sellsBeerRepo.get_price(bill.getBar(), transactions.getItem())


		inventoryRepo = InventoryRepo.InventoryRepo()
		#gets all inventory from date and after for a bar and beer
		results = inventoryRepo.getInventoryForToday(bill.getBar(), transactions.getItem(), bill.getDate())
		if len(results) == 0:
			raise Error("no inventory found for the bar")


		#see if can update inventory
		inventoryRepo = InventoryRepo.InventoryRepo()
		#gets all inventory from date and after for a bar and beer
		results = inventoryRepo.getInventory(bill.getBar(), transactions.getItem(), bill.getDate())
		if len(results) == 0:
			raise Error("no inventory found for the bar")

		#see if violates pattern
		results[0].setEndQuantity(int(results[0].getEndQuantity())- int(transactions.getQuantity()))
		if int(results[0].getEndQuantity()) < 0:
				raise Error("Violates Pattern 4: not enough inventory")
		for r in range(1, len(results)):
			results[r].setStartQuantity(int(results[r-1].getEndQuantity()))
			results[r].setEndQuantity(int(results[r].getEndQuantity())-int(transactions.getQuantity()))
			if int(results[r].getEndQuantity()) < 0:
				raise Error("Violates Pattern 4: not enough inventory")

		#doesn't violate pattern 4
		inventoryRepo = InventoryRepo.InventoryRepo()
		#gets all inventory from date and after for a bar and beer
		results = inventoryRepo.getInventory(bill.getBar(), transactions.getItem(), bill.getDate())


		#update inventory
		results[0].setEndQuantity(int(results[0].getEndQuantity())-int(transactions.getQuantity()))
		inventoryService.updateInventory(results[0], results[0].getDate(), results[0].getBar(), results[0].getBeer())
		for r in range(1, len(results)):
			results[r].setStartQuantity(results[r-1].getEndQuantity())
			results[r].setEndQuantity(int(results[r].getEndQuantity()) -int(transactions.getQuantity()))
			inventoryService.updateInventory(results[r], results[r].getDate(), results[r].getBar(), results[r].getBeer())


	transactionsRepo = TransactionsRepo.TransactionsRepo()
	transactionsRepo.insertTransactions(transactions)

	#update bills
	billsRepo = BillsRepo.BillsRepo()
	bill = billsRepo.getBill(transactions.getBillId())
	items_price = float(transactions.getPrice())
	bill.setItemsPrice(items_price + float(bill.getItemsPrice()))
	bill.setTaxPrice(round(float(bill.getItemsPrice())*0.07,2))
	bill.setTotalPrice(float(bill.getItemsPrice())+ float(bill.getTaxPrice())+ float(bill.getTip()))
	billsService.updateBills(bill, bill.getBillId())

	return "success"

def updateTransactions(transactions,oldBillId, oldItem):
	if int(transactions.getQuantity()) <= 0:
		raise Error("Invalid Quantity")
	
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	if transactionsRepo.duplicate_entry(transactions.getBillId(), transactions.getItem()) and (not transactions.getBillId() == oldBillId or not transactions.getItem() == oldItem):
		raise Error("Duplicate Entry")

	billsRepo = BillsRepo.BillsRepo()
	bill = billsRepo.getBillArray(transactions.getBillId())
	if len(bill) == 0:
		raise Error("No bill has been created for this transaction. Please insert a bill and try again.")
	bill = bill[0]

	transactionsRepo = TransactionsRepo.TransactionsRepo()
	trans = transactionsRepo.get_transaction(oldBillId, oldItem)
	if len(trans) == 0:
		raise Error("no transcation found")
	trans = trans[0]

	if transactions.getType() == "food":
		barFoodRepo = BarFoodRepo.BarFoodRepo()
		if not barFoodRepo.barFood_exists(transactions.getItem()):
			raise Error("Food does not exist")
		sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
		if not sellsFoodRepo.bar_sells_food(bill.getBar(),transactions.getItem()):
			raise Error("Bar doesn't sell the food")

		
	if transactions.getType() == "beer":
		beerRepo = BeerRepo.BeerRepo()
		if not beerRepo.beer_exists(transactions.getItem()):
			raise Error("Beer does not exist")

		sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
		if not sellsBeerRepo.bar_sells_beer(bill.getBar(),transactions.getItem()):
			raise Error("Bar doesn't sell the beer")

		# sellsBeerRepo = SellsBeerRepo.SellsBeerRepo()
		# price = sellsBeerRepo.get_price(transactions.getBar(), transactions.getItem())
		# if not price*int(transactions.getQuantity()) == transactions.getPrice():
		# 	raise Error("Incorrect price")


		inventoryRepo = InventoryRepo.InventoryRepo()
		#gets all inventory from date and after for a bar and beer
		results = inventoryRepo.getInventory(bill.getBar(), transactions.getItem(), bill.getDate())
		if len(results) == 0:
			raise Error("no inventory found for the bar")


		#number of the beer trying to sell
		# transactionsRepo = TransactionsRepo.TransactionsRepo()
		# quantity = transactionsRepo.get_quantity(transactions.getBillId(), transactions.getItem())

		quantity = int(transactions.getQuantity()) - int(trans.getQuantity())


		#see if violates pattern
		results[0].setEndQuantity(int(results[0].getEndQuantity()) - quantity)
		if int(results[0].getEndQuantity()) < 0:
				raise Error("Violates Pattern 4: not enough inventory")
		for r in range(1, len(results)):
			results[r].setStartQuantity(results[r-1].getEndQuantity())
			results[r].setEndQuantity(int(results[r].getEndQuantity()) -quantity)
			if int(results[r].getEndQuantity()) < 0:
				raise Error("Violates Pattern 4: not enough inventory")

		#doesn't violate pattern 4
		inventoryRepo = InventoryRepo.InventoryRepo()
		#gets all inventory from date and after for a bar and beer
		results = inventoryRepo.getInventory(bill.getBar(), transactions.getItem(), bill.getDate())

		#number of the beer trying to sell
		# transactionsRepo = TransactionsRepo.TransactionsRepo()
		# quantity = transactionsRepo.get_quantity(transactions.getBillId(), transactions.getItem())

		#update inventory
		results[0].setEndQuantity(int(results[0].getEndQuantity()) - quantity)
		inventoryService.updateInventory(results[0], results[0].getDate(), results[0].getBar(), results[0].getBeer())
		for r in range(1, len(results)):
			results[r].setStartQuantity(results[r-1].getEndQuantity())
			results[r].setEndQuantity(int(results[r].getEndQuantity()) - quantity)
			inventoryService.updateInventory(results[r], results[r].getDate(), results[r].getBar(), results[r].getBeer())




	
	#update transaction
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	transactionsRepo.updateTransactions(transactions, oldBillId, oldItem)

	#remove all item price from bill
	bill.setItemsPrice(float(bill.getItemsPrice()) - float(trans.getPrice()) )

	#update bills
	items_price = float(bill.getItemsPrice())
	bill.setItemsPrice(items_price + float(transactions.getPrice()))
	bill.setTaxPrice(round(float(bill.getItemsPrice())*0.07,2))
	bill.setTotalPrice(float(bill.getItemsPrice())+ float(bill.getTaxPrice())+ float(bill.getTip()))
	billsService.updateBills(bill, bill.getBillId())

	
	return "success"

''' 
checks:
would need to update bills and maybe inventory
'''
def deleteTransactions(transactions):
	billsRepo = BillsRepo.BillsRepo()
	bill = billsRepo.getBill(transactions.getBillId())
	items_price = float(bill.getItemsPrice())
	bill.setItemsPrice(items_price - float(transactions.getPrice()))
	bill.setTaxPrice(round(float(bill.getItemsPrice())*0.07,2))
	bill.setTotalPrice(float(bill.getItemsPrice())+ float(bill.getTaxPrice())+ float(bill.getTip()))
	billsService.updateBills(bill, bill.getBillId())
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	return transactionsRepo.deleteTransactions(transactions)