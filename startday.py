import shop_money
from customer_class import Customer
import customer_class
import recipes
import pricing
import inventory
import random

numOfBuy = 0
customers_list = []

def startDay():
    soldOut = None
    global customers_list
    global profit
    too_condiment_feedback = 0
    less_condiment_feedback =0
    dense_meat_feedback = 0
    bad_meat_feedback = 0
    price_feedback = 0
    global numOfBuy
    for _ in range(10):
            customer = Customer()
            customers_list.append(customer.get_customer_attributes())
    while True:
        numOfCustomers = 0
        for i in range(random.randint(20,75)):
            if shop_money.meat < recipes.ingredients["meat"] or shop_money.mustard < recipes.ingredients["mustard"] or shop_money.ketchup < recipes.ingredients["ketchup"] or shop_money.buns < 1:
                soldOut = True
                break
            
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
                inventory.inventoryVar["meat"] -= recipes.ingredients["meat"]
                inventory.inventoryVar["mustard"] -= recipes.ingredients["mustard"]
                inventory.inventoryVar["ketchup"] -= recipes.ingredients["ketchup"]
                inventory.inventoryVar["buns"] -= 1
                numOfBuy += 1
        if soldOut == True:
            print("You sold out!")
        profit = float(pricing.pricePer)*numOfBuy
        inventory.inventoryVar["money"] += profit
        print(f"Profit: {profit}")
        print(f"The number of customers that you had was {i}")
        print(f"{too_condiment_feedback} people said you had too many condiments")
        print(f"{less_condiment_feedback} people said you had too many condiments")
        print(f"{dense_meat_feedback} people said you had too dense/high quality ")
        break