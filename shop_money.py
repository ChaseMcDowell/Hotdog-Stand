import startday
money = 100
meat = 0
buns = 0
ketchup = 0
mustard = 0
inventory = {"Money" : money,
             "Meat" : meat,
             "Buns" : buns,
             "Ketchup" : ketchup,
             "Mustard" : mustard}

def shop():
    #making global variables
    global money
    global meat
    global buns
    global ketchup
    global mustard
    global inventory

    while True:#infinite loop so you can purchase many things
        print("Money: " + str(money))
        shopChoice = input("Purchase: \n 1) meat $1 \n 2) buns $.50 \n 3) ketchup $.25 \n 4) mustard $.25 \n 5) Exit shop \n")
        if shopChoice == "5":#exit
            break
        #if they chose meat
        if shopChoice == "1":#purchas meat
            shopAmount = input("How many would you like to buy? ")
            try:
                shopAmount = int(shopAmount)
            except ValueError:
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            money -= int(shopAmount)
            if money < 0:
                money += int(shopAmount)
                print("You cannot afford this!")
            else:
                meat += int(shopAmount)
        #if they choose buns
        elif shopChoice == "2":
            shopAmount = input("How many would you like to buy? ")
            try:
                shopAmount = int(shopAmount)
            except ValueError:
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            money -= 0.5*int(shopAmount)
            if money < 0:
                money += 0.5*int(shopAmount)
                print("You cannot afford this!")
            else:
                buns += int(shopAmount)
        #if they choose ketchup
        elif shopChoice == "3":
            shopAmount = input("How many would you like to buy? ")
            try:
                shopAmount = int(shopAmount)
            except ValueError:
                continue
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            money -= 0.25*int(shopAmount)
            if money < 0:
                money += 0.25*int(shopAmount)
                print("You cannot afford this!")
            else:
                ketchup += int(shopAmount)
        #if they choose mustard
        elif shopChoice == "4":
            shopAmount = input("How many would you like to buy? ")
            try:
                shopAmount = int(shopAmount)
            except ValueError:
                continue 
            if shopAmount <= 0:
                print("Please enter a valid input!")
                continue
            money -= 0.25*int(shopAmount)
            if money < 0:
                money += 0.25*int(shopAmount)
                print("You cannot afford this!")
            else:
                mustard += int(shopAmount)
        else:#if invalid input
            print("Please enter a valid input. ")


# money system don't run the file!!

