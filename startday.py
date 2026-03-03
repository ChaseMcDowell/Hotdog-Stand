import shop_money
from customer_class import Customer
import customer_class
import recipes
import pricing
import inventory
import random

numOfBuy = 0
customers_list = []

def startDay(inventoryVar,ingredients):
    inventoryVar = {"money" : inventoryVar,
             "meat" : inventoryVar,
             "buns" : inventoryVar,
             "ketchup" : inventoryVar,
             "mustard" : inventoryVar}
    ingredients = {"meat":1,
               "ketchup":1,
               "mustard":1}    
    soldOut = None
    global customers_list
    global profit
    too_condiment_feedback = 0
    less_condiment_feedback =0
    dense_meat_feedback = 0
    bad_meat_feedback = 0
    price_feedback = 0
    global numOfBuy
    global customerInLine
    for _ in range(10):
            customer = Customer()
            customers_list.append(customer.get_customer_attributes())
            customerInLine = random.choice(customers_list)
    while True:
        for i in range(random.randint(20,75)):
            if inventoryVar["meat"] < ingredients["meat"] or inventoryVar["mustard"] < ingredients["mustard"] or inventoryVar["ketchup"] < ingredients["ketchup"] or inventoryVar["buns"] < 1:
                soldOut = True
                break
        if ingredients["ketchup"] + ingredients["mustard"] - 1 > customerInLine["condiments"]:
            too_condiment_feedback += 1
        elif ingredients["ketchup"] + ingredients["mustard"] + 1 < customerInLine["condiments"]:
            less_condiment_feedback += 1
        elif ingredients["meat"] - 1 > customerInLine["meat"]:
            dense_meat_feedback += 1
        elif ingredients["meat"] + 1 < customerInLine["meat"]:
            bad_meat_feedback += 1
        elif pricing.pricePer > customerInLine["price"]:
            price_feedback +=1
        else:
            inventoryVar["meat"] -= ingredients["meat"]
            inventoryVar["mustard"] -= ingredients["mustard"]
            inventoryVar["ketchup"] -= ingredients["ketchup"]
            inventoryVar["buns"] -= 1
            numOfBuy += 1
            continue
        if soldOut == True:
            print("You sold out!")
        profit = float(pricing.pricePer)*numOfBuy
        inventoryVar["money"] += profit
        print(f"Profit: {profit}")
        print(f"The number of customers that you had was {i}")
        print(f"{too_condiment_feedback} people said you had too many condiments")
        print(f"{less_condiment_feedback} people said you had too many condiments")
        print(f"{dense_meat_feedback} people said you had too dense/high quality ")
        break
