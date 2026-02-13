import shop_money
inventoryVar = {"money" : shop_money.money,
             "meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}

def inventoryFunc():#function for inventory
    inventoryVar = {"money" : shop_money.money,
             "meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}
    print("Inventory:")
    print("Money: $" + str(inventoryVar["money"]))
    print("Meat: " + str(inventoryVar["meat"]))
    print("Buns: " + str(inventoryVar["buns"]))
    print("Ketchup: " + str(inventoryVar["ketchup"]))
    print("Mustard: " + str(inventoryVar["mustard"]))