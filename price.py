

def price(b, z, x):
    while True:
        costPer = float(b["meat"] + 0.50 + b["ketchup"]*0.25 + b["mustard"]*0.25)
        profitPer = float(x-costPer)
        netProfit = z * profitPer
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Cost per hotdog: {costPer}")
        print(f"Price per hotdog: {x}")
        print(f"Total profit per hotdog: {profitPer}")
        print(f"With your current recipe and inventory, you can produce {z} hotdog(s)")
        priceChoice = input("What would you like to do? \n 1.) Change Price \n 2.) Go Back to Menu \n")
        if priceChoice == "1":
            try:
                x = float(input("How much would you like to charge per hotdog?: "))
            except ValueError:
                print("Please enter a valid input!")
                continue
            if x <= 0:
                print("Please enter a valid input!")
        elif priceChoice == "2":                
            print(f"Cost per hotdog: {costPer}")
            print(f"Price per hotdog: {x}")
            print(f"Total profit per hotdog: {profitPer}")
            print(f"With your current recipe and inventory, you can produce {z} hotdog(s) to profit ${netProfit}")
            break
        else:
            print("Please enter a valid input!")
    return(x)