#game start menu
import shop_money#imports files so it can run the functions
import inventory
import startday

def startMenu():#function for start menu
    while True:#logic for which they select
        gameChoice = input("What would you like to do?: \n 1.) Start Day \n 2.) Inventory \n 3.) Shop \n 4.) Recipes/Pricing \n")
        if gameChoice == "1":
            startday.startDay()
        elif gameChoice == "2":
            inventory.inventoryFunc(shop_money.inventory)
        elif gameChoice == "3":
            shop_money.shop()
        elif gameChoice == "4":
            None
        else:
            print("Please enter valid input!")
