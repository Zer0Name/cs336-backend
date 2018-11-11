import v1.Repos.ShiftsRepo as ShiftsRepo


   
def getLastDate():
    shiftRepo = ShiftsRepo.ShiftsRepo()
    date =  shiftRepo.getLastInsertedDate()

    shiftRepo = ShiftsRepo.ShiftsRepo()
    items = shiftRepo.getLastShifts(date)

    shiftRepo = ShiftsRepo.ShiftsRepo()
    shiftRepo.insertShiftsForToday(items,date)
    return "Success"