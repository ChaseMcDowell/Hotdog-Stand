import shop_money
from customer_class import Customer
import recipes
import pricing
import inventory
import random

buy_noBuy = None
numOfBuy = 0
customers_list = []

def startDay(customers_list):
    for customers_list in range(10):
        customer = Customer()
        customers_list.append(Customer())
    for i in range(random.randint(20,75)):
        customerInLine = random.choice(customers_list)
        if recipes.ingredients["ketchup"] > customerInLine["ketchup"]:
            print("Can I have some hotdog with my ketchup.")
        elif recipes.ingredients["ketchup"] < customerInLine["ketchup"]:
            print("This is dry give me some ketchup.")
        elif recipes.ingredients["meat"] > customerInLine["meat"]:
            print("The meat is to fat. Give me less quality of Meat. ")
        elif recipes.ingredients["meat"] < customerInLine["meat"]:
            print("Why is it green? Give me better meat. ")
        elif recipes.ingredients["mustard"] > customerInLine["mustard"]:
            print("This is too much mustard. You made me throw up.")
        elif recipes.ingredients["mustard"] < customerInLine["mustard"]:
            print("Where is the mustard I asked for.")
        elif pricing.pricePer > customerInLine["price"]:
            print("This is too expensive! Who do you think I am? Elon Musk!")
        else:
            numOfBuy += 1
    math1 = int(pricing.pricePer)*numOfBuy
    print(f"Profit: {math1}")