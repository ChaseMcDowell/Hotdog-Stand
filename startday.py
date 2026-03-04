from customer_class import Customer
import pricing
import random

numOfBuy = 0
customers_list = []

def startDay(x,y):
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
            if int(x["meat"]) < int(y["meat"]) or int(x["mustard"]) < int(y["mustard"]) or int(x["ketchup"]) < int(y["ketchup"]) or int(x["buns"]) < 1:
                soldOut = True
                break
        if y["ketchup"] + y["mustard"] - 1 > customerInLine["condiments"]:
            too_condiment_feedback += 1
        elif y["ketchup"] + y["mustard"] + 1 < customerInLine["condiments"]:
            less_condiment_feedback += 1
        elif y["meat"] - 1 > customerInLine["meat"]:
            dense_meat_feedback += 1
        elif y["meat"] + 1 < customerInLine["meat"]:
            bad_meat_feedback += 1
        elif pricing.pricePer > customerInLine["price"]:
            price_feedback +=1
        else:
            x["meat"] -= y["meat"]
            x["mustard"] -= y["mustard"]
            x["ketchup"] -= y["ketchup"]
            x["buns"] -= 1
            numOfBuy += 1
            continue
        if soldOut == True:
            print("You sold out!")
        profit = float(pricing.pricePer)*numOfBuy
        x["money"] += profit
        print(f"Profit: {profit}")
        print(f"The number of customers that you had was {i}")
        print(f"{too_condiment_feedback} people said you had too many condiments")
        print(f"{less_condiment_feedback} people said you had too many condiments")
        print(f"{dense_meat_feedback} people said you had too dense/high quality ")
        break
