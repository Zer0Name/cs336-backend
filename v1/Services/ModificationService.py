# --------------------- BARTENDER ------------------------------
@modificationController.route('/bartender/insert', methods=['POST'])
def insertBartendertender():
	bartender = Bartender()
	bartender.requestMap(request.get_json())
	return BartenderService.insertBartendertender(bartender)

@modificationController.route('/bartender/update', methods=['POST'])
def updateBartendertender():
	bartender = Bartender()
	req = request.get_json()
	bartender.requestMap(req)
	oldName = str(req.get('old_name'))
	if variable.isEmpty(oldName) :
		raise MissingParamaters("Missing parameter")
	return BartenderService.updateBartendertender(bartender,oldName)

@modificationController.route('/bartender/delete', methods=['POST'])
def deleteBartendertender():
	bartender = Bartender()
	bartender.requestMap(request.get_json())
	return BartenderService.deleteBartendertender(bartender)

# ----------------SERVICE--------------------------------------------------------------------

'''
checks to make:
No bartender can have the same name
check is implemented in table

Check that no drinker has the same name (and phone number?)
'''
def insertBartender(bartender):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.insertBartender(bartender)

'''
checks to make:
No bartender can have the same name 
check is implemented in table

Check that no drinker has the same name (and phone number?)
'''
def updateBartender(bartender,oldName):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.updateBartender(bartender,oldName)

''' no check cascade should be handled by table '''
def deleteBartender(bartender):
	bartenderRepo = BartenderRepo.BartenderRepo()
	return bartenderRepo.deleteBartender(bartender)
#------------------------repo----------------------------------------

	def insertBartender(self,bartender):
		sql = "INSERT INTO Bartender (name, phone, state) VALUES (%s,%s, %s)"
		vals = (bartender.getName(), bartender.getPhone(), bartender.getState())
		return self.insert(sql,vals)


	def updateBartender(self,bartender,oldName):
		sql = "UPDATE Bartender SET name = %s, phone =%s, state = %s WHERE name = %s "
		vals = (bartender.getName(), bartender.getPhone(), bartender.getState(), oldName)
		return self.update(sql,vals)

	def deleteBartender(self,bartender):
		sql = "DELETE FROM Bartender WHERE name = %s "
		vals = (bartender.getName(),)
		return self.delete(sql,vals)
