import shop_money

def inventoryFunc(inventoryVar):#function for inventory
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Inventory:")
    print("Money: $" + str(inventoryVar["money"]))
    print("Meat: " + str(inventoryVar["meat"]))
    print("Buns: " + str(inventoryVar["buns"]))
    print("Ketchup: " + str(inventoryVar["ketchup"]))
    print("Mustard: " + str(inventoryVar["mustard"]))