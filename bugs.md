These are the bugs in the game 

1. Traceback (most recent call last):
  File "game.py", line 2, in <module>
    menu.startMenu() #does the start menu function
  File "C:\Users\gh550414\Documents\GitHub\Hotdog-Stand\menu.py", line 21, in startMenu
    pricing.price(recipes.ingredients,inventory.inventory)
  File "C:\Users\gh550414\Documents\GitHub\Hotdog-Stand\pricing.py", line 24, in price
    print(f"Total profit per hotdog: {pricePer-costPer}")
TypeError: unsupported operand type(s) for -: 'str' and 'float'

1. is fixed -Davis

desc. i was in pricing and tired to make it $2.50 and when i added the cents it gave me this error