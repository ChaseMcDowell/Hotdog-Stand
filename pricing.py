import recipes
import inventory
import shop_money
pricePer = float
pricePer = 3

def price(ingredients,inventoryVar):
    global pricePer
    global pricePer
    while True:
        loop_produce_use = {"meat":inventoryVar["meat"],
                            "ketchup":inventoryVar["ketchup"],
                            "mustard":inventoryVar["mustard"],
                            "buns":inventoryVar["buns"]}
        costPer = float(ingredients["meat"] + 0.50 + ingredients["ketchup"]*0.25 + ingredients["mustard"]*0.25)
        numOfMake = 0
        for numOfMake in range(loop_produce_use["buns"] + 1):
                loop_produce_use["meat"] -= ingredients["meat"]
                loop_produce_use["ketchup"] -= ingredients["ketchup"]
                loop_produce_use["mustard"] -= ingredients["mustard"]
                loop_produce_use["buns"] -= 1
                if loop_produce_use["buns"] >= 0 and loop_produce_use["ketchup"] >= 0 and loop_produce_use["meat"] >= 0 and loop_produce_use["mustard"]:
                    numOfMake += 1
                else:
                    break
        profitPer = float(pricePer-costPer)
        netProfit = numOfMake * profitPer
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Cost per hotdog: {costPer}")
        print(f"Price per hotdog: {pricePer}")
        print(f"Total profit per hotdog: {profitPer}")
        print(f"With your current recipe and inventory, you can produce {numOfMake} hotdog(s) to profit ${netProfit}")
        priceChoice = input("What would you like to do? \n 1.) Change Price \n 2.) Go Back to Menu \n")
        if priceChoice == "1":
            try:
                pricePer = float(input("How much would you like to charge per hotdog?: "))
            except ValueError:
                print("Please enter a valid input!")
                continue
            if pricePer <= 0:
                print("Please enter a valid input!")
        elif priceChoice == "2":
            break
        else:
            print("Please enter a valid input!")

        return numOfMake