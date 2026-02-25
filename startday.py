import shop_money
from customer_class import Customer
import customer_class
import recipes
import pricing
import inventory
import random

numOfBuy = 0
customers_list = []

def startDay(customers_list):
    too_condiment_feedback = 0
    less_condiment_feedback =0
    dense_meat_feedback = 0
    bad_meat_feedback = 0
    price_feedback = 0
    global numOfBuy
    while inventory.inventory["meat"] > 0 and inventory.inventory["ketchup"] > 0 and inventory.inventory["mustard"] > 0:
        if inventory.inventory["meat"] == 0 and inventory.inventory["ketchup"] == 0 and inventory.inventory["mustard"] == 0:
            break
        for _ in range(10):
            customer = Customer()
            customers_list.append(customer.get_customer_attributes())
        for i in range(random.randint(20,75)):
            customerInLine = random.choice(customers_list)
            if recipes.ingredients["ketchup"] + recipes.ingredients["mustard"] - 1 > customerInLine["condiments"]:
                too_condiment_feedback += 1
            elif recipes.ingredients["ketchup"] + recipes.ingredients["mustard"] + 1 < customerInLine["condiments"]:
                less_condiment_feedback += 1
            elif recipes.ingredients["meat"] - 1 > customerInLine["meat"]:
                dense_meat_feedback += 1
            elif recipes.ingredients["meat"] + 1 < customerInLine["meat"]:
                bad_meat_feedback += 1
            elif pricing.pricePer > customerInLine["price"]:
                price_feedback +=1
            else:
                numOfBuy += 1
    profit = int(pricing.pricePer)*numOfBuy
    print(f"Profit: {profit}")
    print(f"The number of customers that you had was {i}")