import shop_money
global recipe
global ingredients
ingredients = {"meat":1,
               "ketchup":1,
               "mustard":1}

def recipe(ingredients):
    while True:
        ingredient_choice = input("Recipe options: \n 1) meat \n 2) ketchup \n 3) mustard \n 4) Exit shop \n")
        if ingredient_choice == "4":
            print("The amount of meat you are using per hotdog is ",ingredients["meat"])
            print("The amount of ketchup you are using per hotdog is ",ingredients["ketchup"])
            print("The amount of mustard you are using per hotdog is ",ingredients["mustard"])
            break
        if ingredient_choice == "1":
            recipe_choice = input("How much meat would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                recipe_choice = ingredients["meat"]
            elif recipe_choice == "2":
                recipe_choice = ingredients["meat"]
            elif recipe_choice == "3":
                recipe_choice = ingredients["meat"]
            else:
                print("Please enter valid input.")
                continue
        if ingredient_choice == "2":
            recipe_choice = input("How much ketchup would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                recipe_choice = ingredients["ketchup"]
            elif recipe_choice == "2":
                recipe_choice = ingredients["ketchup"]
            elif recipe_choice == "3":
                recipe_choice = ingredients["ketchup"]
            else:
                print("Please enter valid input.")
                continue
        if ingredient_choice == "3":
            recipe_choice = input("How much mustard would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                recipe_choice = ingredients["mustard"]
            elif recipe_choice == "2":
                recipe_choice = ingredients["mustard"]
            elif recipe_choice == "3":
                recipe_choice = ingredients["mustard"]
            else:
                print("Please enter valid input.")
                continue
        else:
            print("Please enter a valid input. ")
            continue

recipe(ingredients)