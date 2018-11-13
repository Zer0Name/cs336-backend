
def isEmpty(var):
    if(var == None or var == '' or var == "None"):
        return True
    return False

def isEmptyArray(var):
    if(var == None or len(var) == 0):
        return True
    return False
