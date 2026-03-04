import shop_money

def inventoryFunc(e):#function for inventory
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Inventory:")
    print("Money: $" + str(e["money"]))
    print("Meat: " + str(e["meat"]))
    print("Buns: " + str(e["buns"]))
    print("Ketchup: " + str(e["ketchup"]))
    print("Mustard: " + str(e["mustard"]))