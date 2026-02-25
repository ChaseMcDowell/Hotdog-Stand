#game start menu
import shop_money
import inventory
import startday
import recipes
import pricing

def startMenu():#function for start menu
    while True:#logic for which they select
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        gameChoice = input("What would you like to do?: \n 1.) Start Day \n 2.) Inventory \n 3.) Shop \n 4.) Recipes \n 5.) Pricing \n")
        if gameChoice == "1":
            startday.startDay()
        elif gameChoice == "2":
            inventory.inventoryFunc()
        elif gameChoice == "3":
            shop_money.shop()
        elif gameChoice == "4":
            recipes.recipe(recipes.ingredients)
        elif gameChoice == "5":
            pricing.price(recipes.ingredients)
        else:
            print("Please enter valid input!")