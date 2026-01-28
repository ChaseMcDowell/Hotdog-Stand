import shop_money

def startDay():
    global dailyEarnings
    dailyEarnings = 60
    shop_money.money += dailyEarnings
    print("Daily Earnings: $" + str(dailyEarnings))