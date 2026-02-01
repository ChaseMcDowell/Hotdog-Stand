import shop_money
inventory = {"money" : shop_money.money,
             "meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}

def inventoryFunc(inventory):#function for inventory
    inventory = {"money" : shop_money.money,
             "meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}
    print("Inventory:")
    print("Money: $" + str(inventory["money"]))
    print("Meat: " + str(inventory["meat"]))
    print("Buns: " + str(inventory["buns"]))
    print("Ketchup: " + str(inventory["ketchup"]))
    print("Mustard: " + str(inventory["mustard"]))