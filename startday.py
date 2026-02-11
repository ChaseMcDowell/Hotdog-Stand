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
            print("Can I have some hotdog with my ketchup.")
        elif recipes.ingredients["ketchup"] < customerInLine["ketchup"]:
            print("This is dry give me some ketchup.")
        elif recipes.ingredients["meat"] > customerInLine["meat"]:
            print("I ate half of it. TOO MUCH MEAT!")
        elif recipes.ingredients["meat"] < customerInLine["meat"]:
            print("Where's the beef?")
        elif recipes.ingredients["mustard"] > customerInLine["mustard"]:
            print("This is too much mustard. You made me throw up.")
        elif recipes.ingredients["mustard"] < customerInLine["mustard"]:
            print("Where is the mustard I asked for.")
        elif recipes.ingredients["price"] > customerInLine["price"]:
            print("This is too expensive! Who do you think I am? Elon Musk!")
        else:
            numOfBuy += 1
    
    
    
    
    
    
    
    
    
    
    #this is the end
    #math1 = int(pricing.pricePer)*numOfBuy
    #print(f"Profit: {math1}")