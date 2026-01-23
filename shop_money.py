import startday
global money
money = 100
global meat
meat = 0
global buns
buns = 0
global ketchup
ketchup = 0

def shop():
    #making global variables
    global money
    global meat
    global buns
    global ketchup
    
    while True:#infinite loop so you can purchase many things
        print("Money: " + str(money))
        shopChoice = input("Purchase: \n 1) meat $1 \n 2) buns $.50 \n 3) ketchup $.25 \n 4) Exit shop \n")
        if shopChoice == "4":#exit
            break
        #if they chose meat
        if shopChoice == "1":#purchas meat
            shopAmount = input("How many would you like to buy? ")
            money -= int(shopAmount)
            if money < 0:
                money += int(shopAmount)
                print("You cannot afford this!")
            else:
                meat += int(shopAmount)
        #if they choose buns
        elif shopChoice == "2":
            shopAmount = input("How many would you like to buy? ")
            money -= 0.5*int(shopAmount)
            if money < 0:
                money += 0.5*int(shopAmount)
                print("You cannot afford this!")
            else:
                buns += int(shopAmount)
        #if they choose ketchup
        elif shopChoice == "3":
            shopAmount = input("How many would you like to buy? ")
            money -= 0.25*int(shopAmount)
            if money < 0:
                money += 0.25*int(shopAmount)
                print("You cannot afford this!")
            else:
                ketchup += int(shopAmount)        
        else:#if invalid input
            print("Please enter a valid input. ")

