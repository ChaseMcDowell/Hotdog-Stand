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

    shopChoice = int(input("Purchase: \n 1) meat $1 \n 2) buns $.50 \n 3) ketchup $.25"))
    shopAmount = int(input("How many would you like to buy? "))
    if shopChoice == 1:
        money -= shopAmount
        if money < 0:
            money += shopAmount