import shop_money

global dailyEarnings

def startDay():
    global dailyEarnings
    dailyEarnings = 60
    shop_money.money += dailyEarnings
    print("Daily Earnings: $" + str(dailyEarnings))