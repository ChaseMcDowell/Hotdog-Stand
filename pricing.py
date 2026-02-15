import recipes
import inventory
import shop_money
pricePer = float
pricePer = 3

def price(ingredients):
    global inventory
    produce = {"meat" : shop_money.meat,
             "buns" : shop_money.buns,
             "ketchup" : shop_money.ketchup,
             "mustard" : shop_money.mustard}
    while True:
        global pricePer
        costPer = float(ingredients["meat"] + 0.50 + ingredients["ketchup"]*0.25 + ingredients["mustard"]*0.25)
        numOfMake = 0
        for numOfMake in range(produce["buns"]):
                produce["meat"] -= ingredients["meat"]
                produce["ketchup"] -= ingredients["ketchup"]
                produce["mustard"] -= ingredients["mustard"]
                produce["buns"] -= 1
                if produce["buns"] >= 0 and produce["ketchup"] >= 0 and produce["meat"] >= 0 and produce["mustard"]:
                    numOfMake += 1
                else:
                    break
        grossProfit = numOfMake * pricePer
        netProfit = grossProfit - costPer
        print(numOfMake)
        print(f"Cost per hotdog: {costPer}")
        print(f"Price per hotdog: {pricePer}")
        print(f"Total profit per hotdog: {float(pricePer)-costPer}")
        print(f"With your current recipe and inventory, you can produce {numOfMake} hotdog(s) to profit ${netProfit}")
        priceChoice = input("What would you like to do? \n 1.) Change Price \n 2.) Go Back to Menu \n")
        if priceChoice == "1":
            try:
                pricePer = input("How much would you like to charge per hotdog?: ")
            except ValueError:
                print("Please enter a valid input!")
                continue
            if pricePer <=0:
                print("Please enter a valid input!")
        elif priceChoice == "2":
            break
        else:
            print("Please enter a valid input!")