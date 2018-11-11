from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.TransactionsRepo as TransactionsRepo

def getAllTransactions():
    transactionsRepo = TransactionsRepo.TransactionsRepo() 
    results = transactionsRepo.getAllTransactions()
    return  jsonify([e.toJson() for e in results])

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
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	return transactionsRepo.insertTransactions(transactions)

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
def updateTransactions(transactions,oldBillId, oldItem):
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	return transactionsRepo.updateTransactions(transactions, oldBillId, oldItem)

''' 
checks:
would need to update bills and maybe inventory
'''
def deleteTransactions(transactions):
	transactionsRepo = TransactionsRepo.TransactionsRepo()
	return transactionsRepo.deleteTransactions(transactions)