from flask import Flask, jsonify, Blueprint, request, json, make_response
import v1.Repos.ManufacturerRepo as ManufacturerRepo

def getAllManufacturers():
	manufacturerRepo = ManufacturerRepo.ManufacturerRepo()
	results = manufacturerRepo.getAllManufacturers()
	return  jsonify([e.toJson() for e in results])

def getAllBeersByManufacturer(manf):
	manufacturerRepo = ManufacturerRepo.ManufacturerRepo()
	results = manufacturerRepo.getAllBeersByManufacturer(manf)
	return  jsonify([e.toJson() for e in results])

def getTop10StatesWithHighestSalesInTheLastWeek(manf):
	manufacturerRepo = ManufacturerRepo.ManufacturerRepo()
	results = manufacturerRepo.getTop10StatesWithHighestSalesInTheLastWeek(manf)
	return  jsonify([e.toJson() for e in results])

def getTop10StatesWhereTheirBeerIsLikedTheMost(manf):
	manufacturerRepo = ManufacturerRepo.ManufacturerRepo()
	results = manufacturerRepo.getTop10StatesWhereTheirBeerIsLikedTheMost(manf)
	return  jsonify([e.toJson() for e in results])

