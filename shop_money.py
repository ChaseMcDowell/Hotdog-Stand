
def shop(d):
    while True:#infinite loop so you can purchase many things
        print(f"Money: {d["money"]}")
        shopChoice = input("Purchase: \n 1) meat $1 \n 2) buns $.50 \n 3) ketchup $.25 \n 4) mustard $.25 \n 5) Exit shop \n")
        if shopChoice == "5":#exit
            break
        #if they chose meat
        if shopChoice == "1":#purchas meat
            try:
                shopAmount = int(input("How many would you like to buy? "))
            except ValueError:
                print("Please enter a valid input!")
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            d["money"] -= int(shopAmount)
            if d["money"] < 0:
                d["money"] += int(shopAmount)
                print("You cannot afford this!")
            else:
                d["meat"] += int(shopAmount)
        #if they choose buns
        elif shopChoice == "2":
            try:
                shopAmount = int(input("How many would you like to buy? "))
            except ValueError:
                print("Please enter a valid input!")
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            d["money"] -= 0.5*int(shopAmount)
            if d["money"] < 0:
                d["money"] += 0.5*int(shopAmount)
                print("You cannot afford this!")
            else:
                d["buns"] += int(shopAmount)
        #if they choose ketchup
        elif shopChoice == "3":
            try:
                shopAmount = int(input("How many would you like to buy? "))
            except ValueError:
                print("Please enter a valid input!")
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            d["money"] -= 0.25*int(shopAmount)
            if d["money"] < 0:
                d["money"] += 0.25*int(shopAmount)
                print("You cannot afford this!")
            else:
                d["ketchup"] += int(shopAmount)
        #if they choose mustard
        elif shopChoice == "4":
            try:
                shopAmount = int(input("How many would you like to buy? "))
            except ValueError:
                print("Please enter a valid input!")
                continue 
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            d["money"] -= 0.25*int(shopAmount)
            if d["money"] < 0:
                d["money"] += 0.25*int(shopAmount)
                print("You cannot afford this!")
            else:
                d["mustard"] += int(shopAmount)
        else:#if invalid input
            print("Please enter a valid input. ")


# money system don't run the file!!