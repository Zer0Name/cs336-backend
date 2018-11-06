import mysql.connector
import v1.Repos.DrinkersRepo as DrinkerRepo

'''
checks to make:
No drinker can have the same name
'''
def insertDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.insertDrinker(drinker)

def updateDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.updateDrinker(drinker)

def deleteDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.deleteDrinker(drinker)

