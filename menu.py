#game start menu
import shop_money
import inventory
import startday
import recipes
import pricing

def startMenu():#function for start menu
    inventoryVar = {"money" : shop_money.money,
             "meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}
    ingredients = {"meat":1,
               "ketchup":1,
               "mustard":1}
    while True:#logic for which they select
        if inventoryVar["money"] == 0 and pricing.numOfMake == 0:
            print("You lose")
            break
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        gameChoice = input("What would you like to do?: \n 1.) Start Day \n 2.) Inventory \n 3.) Shop \n 4.) Recipes \n 5.) Pricing \n")
        if gameChoice == "1":
            startday.startDay(ingredients,inventoryVar)
        elif gameChoice == "2":
            inventory.inventoryFunc(inventoryVar)
        elif gameChoice == "3":
            shop_money.shop()
        elif gameChoice == "4":
            recipes.recipe(ingredients)
        elif gameChoice == "5":
            pricing.price(ingredients)
        elif gameChoice != "1" or gameChoice != "2" or gameChoice != "3" or gameChoice != "4" or gameChoice != "5":
            print("Please enter valid input!")
            continue
        if inventoryVar["money"] == 0 and pricing.numOfMake == 0:
            break
        