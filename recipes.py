


def recipe(c):
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ingredient_choice = input("Recipe options: \n 1) meat \n 2) ketchup \n 3) mustard \n 4) Exit recipes \n")
        if c["meat"] == 3:
            qual = "wagyu"
        if c["meat"] == 2:
            qual = "prime"
        if c["meat"] == 1:
            qual = "choice"
        if qual == "choice":
            rMeat = 1
        if qual == "wagyu":
            rMeat = 3
        if qual == "prime":
            rMeat = 2
        if ingredient_choice == "4":
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("The quality of meat you are using per hotdog is", qual + ". This will use",rMeat,"meat per hotdog.")
            print("The amount of ketchup you are using per hotdog is ",str(c["ketchup"]))
            print("The amount of mustard you are using per hotdog is ",str(c["mustard"]))
            break
        elif ingredient_choice == "1":
            recipe_choice = input("What quality of meat would you like to use meat would you like to use.\n 1) Wagyu (Best quality, Most Meat) \n 2) Prime (Middle quality, Middle Amount of Meat) \n 3) Choice (Lowest Quality, Least Amount of Meat) \n ")
            if recipe_choice == "1":
                c["meat"] = 3
            elif recipe_choice == "2":
                c["meat"] = 2
            elif recipe_choice == "3":
                c["meat"] = 1
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Please enter valid input.")
                continue
        elif ingredient_choice == "2":
            ket_recipe_choice = input("How much ketchup would you like to use. (1,2,3) ")
            if ket_recipe_choice == "1":
                c["ketchup"] = 1
            elif ket_recipe_choice == "2":
                c["ketchup"] = 2
            elif ket_recipe_choice == "3":
                c["ketchup"] = 3
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Please enter valid input.")
                continue
        elif ingredient_choice == "3":
            mus_recipe_choice = input("How much mustard would you like to use. (1,2,3) ")
            if mus_recipe_choice == "1":
                c["mustard"] = 1
            elif mus_recipe_choice == "2":
                c["mustard"] = 2
            elif mus_recipe_choice == "3":
                c["mustard"] = 3
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Please enter valid input.")
                continue
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Please enter a valid input. ")
            continue
    return(c)