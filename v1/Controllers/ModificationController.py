from flask import Flask, jsonify, Blueprint, request, json, make_response
import datetime
import v1.Util.Variable as variable
from v1.Exceptions.MissingParamaters import MissingParamaters

import v1.Services.BeerService as beerService
import v1.Services.BarService as barService
import v1.Services.BartenderService as bartenderService
import v1.Services.DrinkerService as drinkerService
import v1.Services.BarFoodService as barFoodService
import v1.Services.DayService as dayService
import v1.Services.FrequentsService as frequentsService
import v1.Services.LikesService as likesService
import v1.Services.SellsBeerService as sellsBeerService
import v1.Services.SellsFoodService as sellsFoodService
import v1.Services.OperatesService as operatesService
import v1.Services.InventoryService as inventoryService


from v1.Entity.Drinker import Drinker
from v1.Entity.Beer import Beer
from v1.Entity.Bar import Bar
from v1.Entity.Bartender import Bartender
from v1.Entity.BarFood import BarFood
from v1.Entity.Day import Day
from v1.Entity.Frequents import Frequents
from v1.Entity.Likes import Likes
from v1.Entity.SellsBeer import SellsBeer
from v1.Entity.SellsFood import SellsFood
from v1.Entity.Operates import Operates
from v1.Entity.Inventory import Inventory


modificationController = Blueprint('modificationController', __name__)



# --------------------- DRINKER ------------------------------
@modificationController.route('/drinker/insert', methods=['POST'])
def insertDrinker():
	drinker = Drinker()
	drinker.requestMap(request.get_json())
	return drinkerService.insertDrinker(drinker)

@modificationController.route('/drinker/update', methods=['POST'])
def updateDrinker():
	drinker = Drinker()
	req = request.get_json()
	drinker.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return drinkerService.updateDrinker(drinker,oldName)

@modificationController.route('/drinker/delete', methods=['POST'])
def deleteDrinker():
	drinker = Drinker()
	drinker.requestMap(request.get_json())
	return drinkerService.deleteDrinker(drinker)

# --------------------- BEER ------------------------------
@modificationController.route('/beer/insert', methods=['POST'])
def insertBeer():
	beer = Beer()
	beer.requestMap(request.get_json())
	return beerService.insertBeer(beer)

@modificationController.route('/beer/update', methods=['POST'])
def updateBeer():
	beer = Beer()
	req = request.get_json()
	beer.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return beerService.updateBeer(beer,oldName)

@modificationController.route('/beer/delete', methods=['POST'])
def deleteBeer():
	beer = Beer()
	beer.requestMap(request.get_json())
	return beerService.deleteBeer(beer)

# --------------------- BAR ------------------------------
@modificationController.route('/bar/insert', methods=['POST'])
def insertBar():
	bar = Bar()
	bar.requestMap(request.get_json())
	return barService.insertBar(bar)

@modificationController.route('/bar/update', methods=['POST'])
def updateBar():
	bar = Bar()
	req = request.get_json()
	bar.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return barService.updateBar(bar,oldName)

@modificationController.route('/bar/delete', methods=['POST'])
def deleteBar():
	bar = Bar()
	bar.requestMap(request.get_json())
	return barService.deleteBar(bar)

# --------------------- BARTENDER ------------------------------
@modificationController.route('/bartender/insert', methods=['POST'])
def insertBartender():
	bartender = Bartender()
	bartender.requestMap(request.get_json())
	return bartenderService.insertBartender(bartender)

@modificationController.route('/bartender/update', methods=['POST'])
def updateBartender():
	bartender = Bartender()
	req = request.get_json()
	bartender.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return bartenderService.updateBartender(bartender,oldName)

@modificationController.route('/bartender/delete', methods=['POST'])
def deleteBartender():
	bartender = Bartender()
	bartender.requestMap(request.get_json())
	return bartenderService.deleteBartender(bartender)

# --------------------- BAR FOOD------------------------------
@modificationController.route('/barfood/insert', methods=['POST'])
def insertBarFood():
	barFood = BarFood()
	barFood.requestMap(request.get_json())
	return barFoodService.insertBarFood(barFood)

@modificationController.route('/barfood/update', methods=['POST'])
def updateBarFood():
	barFood = BarFood()
	req = request.get_json()
	barFood.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return barFoodService.updateBarFood(barFood,oldName)

@modificationController.route('/barfood/delete', methods=['POST'])
def deleteBarFood():
	barFood = BarFood()
	barFood.requestMap(request.get_json())
	return barFoodService.deleteBarFood(barFood)

# --------------------- DAY ------------------------------
@modificationController.route('/day/insert', methods=['POST'])
def insertDay():
	day = Day()
	day.requestMap(request.get_json())
	return dayService.insertDay(day)

@modificationController.route('/day/update', methods=['POST'])
def updateDay():
	day = Day()
	req = request.get_json()
	day.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return dayService.updateDay(day,oldName)

@modificationController.route('/day/delete', methods=['POST'])
def deleteDay():
	day = Day()
	day.requestMap(request.get_json())
	return dayService.deleteDay(day)

# --------------------- FREQUENTS ------------------------------
@modificationController.route('/frequents/insert', methods=['POST'])
def insertFrequents():
	frequents = Frequents()
	frequents.requestMap(request.get_json())
	return frequentsService.insertFrequents(frequents)

@modificationController.route('/frequents/update', methods=['POST'])
def updateFrequents():
	frequents = Frequents()
	req = request.get_json()
	frequents.requestMap(req)
	oldDrinker = str(req.get('old_drinker'))
	oldBar = str(req.get('old_bar'))
	if variable.isEmpty(oldDrinker) or variable.isEmpty(oldBar):
		raise MissingParamaters("Missing parameter")
	return frequentsService.updateFrequents(frequents, oldDrinker, oldBar)

@modificationController.route('/frequents/delete', methods=['POST'])
def deleteFrequents():
	frequents = Frequents()
	frequents.requestMap(request.get_json())
	return frequentsService.deleteFrequents(frequents)

# --------------------- LIKES ------------------------------
@modificationController.route('/likes/insert', methods=['POST'])
def insertLikes():
	likes = Likes()
	likes.requestMap(request.get_json())
	return likesService.insertLikes(likes)

@modificationController.route('/likes/update', methods=['POST'])
def updateLikes():
	likes = Likes()
	req = request.get_json()
	likes.requestMap(req)
	oldDrinker = str(req.get('old_drinker'))
	oldBeer = str(req.get('old_beer'))
	if variable.isEmpty(oldDrinker) or variable.isEmpty(oldBeer):
		raise MissingParamaters("Missing parameter")
	return likesService.updateLikes(likes, oldDrinker, oldBeer)

@modificationController.route('/likes/delete', methods=['POST'])
def deleteLikes():
	likes = Likes()
	likes.requestMap(request.get_json())
	return likesService.deleteLikes(likes)

# --------------------- SELLSBEER ------------------------------
@modificationController.route('/sellsBeer/insert', methods=['POST'])
def insertSellsBeer():
	sellsBeer = SellsBeer()
	sellsBeer.requestMap(request.get_json())
	return sellsBeerService.insertSellsBeer(sellsBeer)

@modificationController.route('/sellsBeer/update', methods=['POST'])
def updateSellsBeer():
	sellsBeer = SellsBeer()
	req = request.get_json()
	sellsBeer.requestMap(req)
	oldBar = str(req.get('old_bar'))
	oldBeer = str(req.get('old_beer'))
	if variable.isEmpty(oldBar) or variable.isEmpty(oldBeer):
		raise MissingParamaters("Missing parameter")
	return sellsBeerService.updateSellsBeer(sellsBeer, oldBeer, oldBar)

@modificationController.route('/sellsBeer/delete', methods=['POST'])
def deleteSellsBeer():
	sellsBeer = SellsBeer()
	sellsBeer.requestMap(request.get_json())
	return sellsBeerService.deleteSellsBeer(sellsBeer)

# --------------------- SELLSFOOD ------------------------------
@modificationController.route('/sellsFood/insert', methods=['POST'])
def insertSellsFood():
	sellsFood = SellsFood()
	sellsFood.requestMap(request.get_json())
	return sellsFoodService.insertSellsFood(sellsFood)

@modificationController.route('/sellsFood/update', methods=['POST'])
def updateSellsFood():
	sellsFood = SellsFood()
	req = request.get_json()
	sellsFood.requestMap(req)
	oldBar = str(req.get('old_bar'))
	oldFood = str(req.get('old_food'))
	if variable.isEmpty(oldBar) or variable.isEmpty(oldFood):
		raise MissingParamaters("Missing parameter")
	return sellsFoodService.updateSellsFood(sellsFood, oldFood, oldBar)

@modificationController.route('/sellsFood/delete', methods=['POST'])
def deleteSellsFood():
	sellsFood = SellsFood()
	sellsFood.requestMap(request.get_json())
	return sellsFoodService.deleteSellsFood(sellsFood)

# --------------------- OPERATES ------------------------------
@modificationController.route('/operates/insert', methods=['POST'])
def insertOperates():
	operates = Operates()
	operates.requestMap(request.get_json())
	return operatesService.insertOperates(operates)

@modificationController.route('/operates/update', methods=['POST'])
def updateOperates():
	operates = Operates()
	req = request.get_json()
	operates.requestMap(req)
	oldBar = str(req.get('old_bar'))
	oldDay = str(req.get('old_day'))
	if variable.isEmpty(oldBar) or variable.isEmpty(oldDay):
		raise MissingParamaters("Missing parameter")
	return operatesService.updateOperates(operates, oldDay, oldBar)

@modificationController.route('/operates/delete', methods=['POST'])
def deleteOperates():
	operates = Operates()
	operates.requestMap(request.get_json())
	return operatesService.deleteOperates(operates)

# --------------------- INVENTORY ------------------------------
@modificationController.route('/inventory/insert', methods=['POST'])
def insertInventory():
	inventory = Inventory()
	inventory.requestMap(request.get_json())
	return inventoryService.insertInventory(inventory)

@modificationController.route('/inventory/update', methods=['POST'])
def updateInventory():
	inventory = Inventory()
	req = request.get_json()
	operates.requestMap(req)
	oldBar = str(req.get('old_bar'))
	oldDate = str(req.get('old_date'))
	oldBeer = str(req.get('old_beer'))
	if variable.isEmpty(oldBar) or variable.isEmpty(oldDate) or variable.isEmpty(oldBeer):
		raise MissingParamaters("Missing parameter")
	return inventoryService.updateInventory(inventory, oldDate, oldBar, oldBeer)

@modificationController.route('/inventory/delete', methods=['POST'])
def deleteInventory():
	inventory = Inventory()
	inventory.requestMap(request.get_json())
	return inventoryService.deleteInventory(inventory)
