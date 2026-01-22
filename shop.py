global money
money = 100
global meat
meat = 0
global buns
buns = 0
global ketchup
ketchup = 0

def shop():
    global money
    global meat
    global buns
    global ketchup

    shopChoice = int(input("Purchase: \n 1) meat $1 \n 2) buns $.50 \n 3) ketchup $.25 \n 4) Exit shop \n"))
    shopAmount = int(input("How many would you like to buy? "))
    #if they chose meat
    if shopChoice == 1:
        money -= shopAmount
        if money < 0:
            money += shopAmount
            print("You cannot afford this!")
            shop()
        else:
            meat += shopAmount
            shop()
    #if they choose buns
    if shopChoice == 2:
        money -= 0.5*shopAmount
        if money < 0:
            money += 0.5*shopAmount
            print("You cannot afford this!")
            shop()
        else:
            buns += shopAmount
            shop()
    #if they choose ketchup
    if shopChoice == 3:
        money -= 0.25*shopAmount
        if money < 0:
            money += 0.25*shopAmount
            print("You cannot afford this!")
            shop()
        else:
            ketchup += shopAmount
            shop()        
    #if they want to leave
    if shopChoice == 4:
        None
    else:
        print("Please enter a valid number")
        shop()
  
shop()
