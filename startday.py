from customer_class import Customer
import random

def startDay(x,y,z,z1):
    numOfBuy = 0
    soldOut = None
    global profit
    too_condiment_feedback = 0
    less_condiment_feedback =0
    dense_meat_feedback = 0
    bad_meat_feedback = 0
    price_feedback = 0
    while True:
        for i in range(random.randint(20,75)):
            customers_list = []
            customer = Customer()
            customers_list.append(customer.get_customer_attributes())
            customerInLine = random.choice(customers_list)
            if z1 < 1:
                soldOut = True
                if soldOut == True:
                    print("You sold out!")
                break
            if y["ketchup"] + y["mustard"] - 1 > customerInLine["condiments"]:
                too_condiment_feedback += 1
                continue
            elif y["ketchup"] + y["mustard"] + 1 < customerInLine["condiments"]:
                less_condiment_feedback += 1
                continue
            elif y["meat"] > customerInLine["meat"]:
                dense_meat_feedback += 1
                continue
            elif y["meat"] < customerInLine["meat"]:
                bad_meat_feedback += 1
                continue
            elif z > customerInLine["price"]:
                price_feedback +=1
                continue
            else:
                x["meat"] -= y["meat"]
                x["mustard"] -= y["mustard"]
                x["ketchup"] -= y["ketchup"]
                x["buns"] -= 1
                numOfBuy += 1
                continue
        profit = float(z)*numOfBuy
        x["money"] += profit
        print(f"Profit: {profit}")
        print(f"The number of customers that you had was {i}")
        print(f"{too_condiment_feedback} people said you had too many condiments")
        print(f"{less_condiment_feedback} people said you had too many condiments")
        print(f"{dense_meat_feedback} people said you had too dense/high quality ")
        print(f"{price_feedback} people said you charged too much")
        break
    return(x,y,z1)