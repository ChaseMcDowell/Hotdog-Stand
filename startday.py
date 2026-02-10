import shop_money
from customer_class import Customer
import recipes
import pricing
import inventory
import random

buy_noBuy = None
numOfBuy = 0
customers = []

def startDay(customers):
    for customers in range(10):
        customers.append(Customer())
    for i in range(random.randint(20,75)):
        customerInLine = random.choice(customers)
        if recipes.ingredients["ketchup"] > customerInLine["ketchup"]:
            print("You were using too much ketchup this is nasty.")
        elif recipes.ingredients["ketchup"] < customerInLine["ketchup"]:
            print("Not enough ketchup for me.")
    
    
    
    
    
    
    
    
    
    
    
    #this is the end
    #math1 = int(pricing.pricePer)*numOfBuy
    #print(f"Profit: {math1}")