import shop_money
from customer_class import Customer
import customer_class
import recipes
import pricing
import inventory
import random

numOfBuy = 0
customers_list = []
preferences = {}

def startDay(customers_list):
    global numOfBuy
    for _ in range(10):
        customer = Customer()
        customers_list.append(customer.get_customer_attributes())
    for i in range(random.randint(20,75)):
        customerInLine = random.choice(customers_list)
        if recipes.ingredients["ketchup"] + recipes.ingredients["mustard"] > customerInLine["condiments"]:
            print("Can I have some hotdog with my sauce. \n")
        elif recipes.ingredients["ketchup"] + recipes.ingredients["mustard"] < customerInLine["condiments"]:
            print("This is dry give me some condiments. \n")
        elif recipes.ingredients["meat"] > customerInLine["meat"]:
            print("The meat is to fat. Give me less quality of Meat. \n")
        elif recipes.ingredients["meat"] < customerInLine["meat"]:
            print("Why is it green? Give me better meat. \n")
        elif pricing.pricePer > customerInLine["price"]:
            print("This is too expensive! Who do you think I am? Elon Musk!")
        else:
            numOfBuy += 1
    math1 = int(pricing.pricePer)*numOfBuy
    print(f"Profit: {math1}")