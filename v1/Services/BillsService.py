from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BillsRepo as BillsRepo

'''
checks to make:
no duplicate entries
if no corresponding bills items price, tax, and total price must be zero?
if corresponding bills items price = total of those bills
bartender works at the bar
bar exists
bartender exists
drinker exists
bill_id is not in the table yet (unique)
make sure the day corresponds to the date
tax is 7% of the items price
total price is items price + tax + tip
time is during bar's hours and during bartender's shift
'''
def insertBills(bills):
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.insertBills(bills)

'''
checks to make:
no duplicate entries
if no corresponding bills items price, tax, and total price must be zero?
if corresponding bills items price = total of those bills
bartender works at the bar
bar exists
bartender exists
drinker exists
bill_id is not in the table yet (unique)
make sure the day corresponds to the date
tax is 7% of the items price
total price is items price + tax + tip
time is during bar's hours and during bartender's shift
'''
def updateBills(bills,oldBillId):
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.updateBills(bills, oldBillId)

''' 
checks:
would need to update bills and maybe inventory
'''
def deleteBills(bills):
	billsRepo = BillsRepo.BillsRepo()
	return billsRepo.deleteBills(bills)