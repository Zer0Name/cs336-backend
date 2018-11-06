import mysql.connector
import v1.Repos.DrinkersRepo as DrinkerRepo



# --------------------- DRINKER ------------------------------
'''
checks to make:
No drinker can have the same name
check is implemented in table
'''
def insertDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.insertDrinker(drinker)
	
'''
checks to make:
No drinker can have the same name
check is implemented in table
'''
def updateDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.updateDrinker(drinker)

''' no check cascade should be handled by table '''
def deleteDrinker(drinker):
	drinkerRepo = DrinkerRepo.DrinkerRepo()
	return drinkerRepo.deleteDrinker(drinker)

