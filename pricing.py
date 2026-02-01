import recipes
import inventory
pricePer = 3

def price(ingredients,inventory):
    while True:
        global pricePer
        costPer = ingredients["meat"] + 0.50 + ingredients["ketchup"]*0.25 + ingredients["mustard"]*0.25
        produce = {"numofmeat" : inventory["meat"] / ingredients["meat"],
                   "numofbuns" : inventory["buns"],
                   "numofketchup" :inventory["ketchup"] / ingredients["ketchup"],
                   "numofmustard" : inventory["mustard"] / ingredients["mustard"]}
        numOfMake = min(produce.values())
        print(f"Cost per hotdog: {costPer}")
        print(f"Price per hotdog: {pricePer}")
        print(f"Total profit per hotdog: {pricePer-costPer}")
        print(f"With your current recipe and inventory, you can produce {numOfMake} hotdog(s) to profit ${numOfMake * pricePer}")
        priceChoice = input("What would you like to do? \n 1.) Change Price \n 2.) Go Back to Menu")
        if priceChoice == "1":
            pricePer = input("How much would you like to charge per hotdog?: ")
            try:
                pricePer = int(pricePer)
            except ValueError:
                print("Please enter a valid input!")
                continue
            if pricePer <=0:
                print("Please enter a valid input!")
        elif priceChoice == "2":
            break
        else:
            print("Please enter a valid input!")