pricePer = float
pricePer = 3

def price(a,b):
    global pricePer
    global pricePer
    while True:
        loopUse = {"meat":a["meat"],
                            "ketchup":a["ketchup"],
                            "mustard":a["mustard"],
                            "buns":a["buns"]}
        costPer = float(b["meat"] + 0.50 + b["ketchup"]*0.25 + b["mustard"]*0.25)
        numOfMake = 0
        for numOfMake in range(loopUse["buns"] + 1):
                loopUse["meat"] -= b["meat"]
                loopUse["ketchup"] -= b["ketchup"]
                loopUse["mustard"] -= b["mustard"]
                loopUse["buns"] -= 1
                if loopUse["buns"] >= 0 and loopUse["ketchup"] >= 0 and loopUse["meat"] >= 0 and loopUse["mustard"]:
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