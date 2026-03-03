import menu#imports menu to run the game
import backstory
import time
import shop_money
import inventory
import startday
import recipes
import pricing

numOfMake = 0

inventoryVar = {"money" : 100,
            "meat" : 0,
            "buns" : 0,
            "ketchup" : 0,
            "mustard" : 0}

ingredients = {"meat":1,
            "ketchup":1,
            "mustard":1}

print("Please fullscreen terminal for the best experience")
#time.sleep(5)
backstory.story_mode()
while True:#logic for which they select
    if inventoryVar["money"] == 0 and numOfMake == 0:
        print("You lose")
        break
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    gameChoice = input("What would you like to do?: \n 1.) Start Day \n 2.) Inventory \n 3.) Shop \n 4.) Recipes \n 5.) Pricing \n")
    if gameChoice == "1":
        startday.startDay(ingredients,inventoryVar)
    elif gameChoice == "2":
        inventory.inventoryFunc(inventoryVar)
    elif gameChoice == "3":
        shop_money.shop(inventoryVar)
    elif gameChoice == "4":
        recipes.recipe(ingredients)
    elif gameChoice == "5":
        numOfMake = pricing.price(ingredients,inventoryVar)
    elif gameChoice != "1" or gameChoice != "2" or gameChoice != "3" or gameChoice != "4" or gameChoice != "5":
        print("Please enter valid input!")
        continue