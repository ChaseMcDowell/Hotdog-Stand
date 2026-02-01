import shop_money
ingredients = {"meat":1,
               "ketchup":1,
               "mustard":1}

def recipe(ingredients):
    while True:
        ingredient_choice = input("Recipe options: \n 1) meat \n 2) ketchup \n 3) mustard \n 4) Exit recipes \n")
        if ingredient_choice == "4":
            print("The amount of meat you are using per hotdog is ",ingredients["meat"])
            print("The amount of ketchup you are using per hotdog is ",ingredients["ketchup"])
            print("The amount of mustard you are using per hotdog is ",ingredients["mustard"])
            break
        elif ingredient_choice == "1":
            recipe_choice = input("How much meat would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                ingredients["meat"] = 1
            elif recipe_choice == "2":
                ingredients["meat"] = 2
            elif recipe_choice == "3":
                ingredients["meat"] = 3
            else:
                print("Please enter valid input.")
                continue
        elif ingredient_choice == "2":
            recipe_choice = input("How much ketchup would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                ingredients["ketchup"] = 1
            elif recipe_choice == "2":
                ingredients["ketchup"] = 2
            elif recipe_choice == "3":
                ingredients["ketchup"] = 3
            else:
                print("Please enter valid input.")
                continue
        elif ingredient_choice == "3":
            recipe_choice = input("How much mustard would you like to use. (1,2,3) ")
            if recipe_choice == "1":
                ingredients["mustard"] = 1
            elif recipe_choice == "2":
                ingredients["mustard"] = 2
            elif recipe_choice == "3":
                ingredients["mustard"] = 3
            else:
                print("Please enter valid input.")
                continue
        else:
            print("Please enter a valid input. ")
            continue


