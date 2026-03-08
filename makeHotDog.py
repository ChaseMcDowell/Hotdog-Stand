def makeHotDog(inven,ingrie,make):
    maxMeat = inven["meat"] // ingrie["meat"]
    maxKetchup = inven["ketchup"] // ingrie["ketchup"]
    maxMustard = inven["mustard"] // ingrie["mustard"]
    maxBuns = inven["buns"]
    make = min(maxMeat,maxKetchup,maxMustard,maxBuns)
    return make