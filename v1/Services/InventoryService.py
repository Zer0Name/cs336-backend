import v1.Repos.InventoryRepo as InventoryRepo


def insertInventoryForToday():
    inventoryRepo = InventoryRepo.InventoryRepo()
    items  = inventoryRepo.getAllInventoryFromYesterday()
    inventoryRepo = InventoryRepo.InventoryRepo()
    inventoryRepo.insertInventoryForToday(items)
    return "success"