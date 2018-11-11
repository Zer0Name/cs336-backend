from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.BarFoodRepo as BarFoodRepo

def getAllBarFood():
    barFoodRepo = BarFoodRepo.BarFoodRepo() 
    results = barFoodRepo.getAllBarFood()
    return  jsonify([e.toJson() for e in results])
	
'''
checks to make:
No barFood can have the same name
check is implemented in table

'''
def insertBarFood(barFood):
	barFoodRepo = BarFoodRepo.BarFoodRepo()
	return barFoodRepo.insertBarFood(barFood)

'''
checks to make:
No barFood can have the same name
check is implemented in table

'''
def updateBarFood(barFood,oldName):
	barFoodRepo = BarFoodRepo.BarFoodRepo()
	return barFoodRepo.updateBarFood(barFood,oldName)

''' no check cascade should be handled by table '''
def deleteBarFood(barFood):
	barFoodRepo = BarFoodRepo.BarFoodRepo()
	return barFoodRepo.deleteBarFood(barFood)
