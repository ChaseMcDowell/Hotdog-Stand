import shop_money
ingredients = {"meat":1,
               "ketchup":1,
               "mustard":1}

def recipe(ingredients):
    while True:
        ingredient_choice = input("Recipe options: \n 1) meat \n 2) ketchup \n 3) mustard \n 4) Exit recipes \n")
        if ingredients["meat"] == 3:
            qual = "wagyu"
        if ingredients["meat"] == 2:
            qual = "prime"
        if ingredients["meat"] == 1:
            qual = "choice"
        if qual == "choice":
            meat_use = 1
        if qual == "wagyu":
            meat_use = 3
        if qual == "prime":
            meat_use = 2
        if ingredient_choice == "4":
            print("The quality of meat you are using per hotdog is", qual + ". This will use ",meat_use," meat per hotdog.")
            print("The amount of ketchup you are using per hotdog is ",str(ingredients["ketchup"]) + ". This will use 2 meat per hotdog.")
            print("The amount of mustard you are using per hotdog is ",str(ingredients["mustard"]) + ". This will use 1 meat per hotdog.")
            break
        elif ingredient_choice == "1":
            recipe_choice = input("What quality of meat would you like to use meat would you like to use.\n 1) Wagyu (Best quality) \n 2) Prime (Middle quality) \n 3) Choice (Lowest quality) \n ")
            if recipe_choice == "1":
                ingredients["meat"] = 3
            elif recipe_choice == "2":
                ingredients["meat"] = 2
            elif recipe_choice == "3":
                ingredients["meat"] = 1
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