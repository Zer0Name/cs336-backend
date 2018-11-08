from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.SellsFoodRepo as SellsFoodRepo

'''
checks to make:
no duplicate entries
Food exists
bar exists
'''
def insertSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.insertSellsFood(sellsFood)

'''
checks to make:
no duplicate entries
Food exists
bar exists
'''
def updateSellsFood(sellsFood,oldFood, oldBar):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.updateSellsFood(sellsFood, oldFood, oldBar)

''' no check cascade should be handled by table '''
def deleteSellsFood(sellsFood):
	sellsFoodRepo = SellsFoodRepo.SellsFoodRepo()
	return sellsFoodRepo.deleteSellsFood(sellsFood)