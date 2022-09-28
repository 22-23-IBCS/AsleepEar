class coffeeShop():

    def __init__(self):
        self.coffee = 4.00
        self.latte = 4.50
        self.hotCider = 3.0
        self.size = ""
        self.sizes = {"small" : 0.45, "medium": 0.60, "large" : 0.80}
        self.drinks = {"coffee" : 4.00, "latte": 4.50, "hot cider": 3.0}
        self.drink = ""

    def getPrice(self, item):
        item = item.lower()
        try:
            return self.drinks[item], item
        except:
            print("Invalid item!")
            option = input("Coffee, Latte, Hot Cider\n")
            return self.getPrice(option)
        return self.drinks[item], item

    def setSize (self):
        option = input("Small, Medium, or Large.\n").lower()
        if (option != "small" and option != "medium" and option != "large"):
            print("Invalid selection!")
            return self.setSize()
        
        return option
        

    def setDrink(self):
        option = input("Coffee, Latte, or Hot Cider.\n").lower()
        if (option != "coffee" and option != "latte" and option != "hot cider"):
            print("Invalid selection!")
            return self.setDrink()
        
        return option
        
        
        
   
def main():


    shop = coffeeShop()
    
    print("Hi, welcome to coffee shop. Please pick an option.")
    greet= int(input("1. Order, 2. getPrice: "))
    if greet == 1:
        price = 0
        print("What would you like to order?")
        option = shop.setDrink()
        print(option)
        
        price += shop.getPrice(option)[0]
        print("What size would you like?\n")
        size = shop.setSize()
        price += shop.sizes[size]
        name = input("What is your name?\n")
        print("Here is your " + option + ", " + name + ". That will be $" + str(price))
        
    elif greet == 2:
        option = input("Coffee, Latte, Hot Cider\n")
        money, option = shop.getPrice(option)
        print("A " + option + " is $" + str(money))
        main()
    
        
        
    

   
        


if __name__ == "__main__":
    main()
