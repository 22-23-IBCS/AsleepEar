import json
import time

class store:

    def __init__(self):

        self.id = {}
        
        try:
            
            self.id = json.load(open("Store Info.json", "rt"))
        except:
            self.storeValues = open("Store Info.json", "w")
            self.firstTimeSetup()



    def firstTimeSetup(self):
        
        print("Hello aspiring entrepreneur!\nWelcome to the interactive store creator!")
        
        self.id["manager"] = input("What is your name?\n")
        self.id["storeName"] = input("What would you like to name your store?\n")
        self.id["salesTax"] = float(input("What is the sales tax in your area? (enter value as decimal)\nEx: \"0.10\"\n"))
        items = {}
        stocks = {}
        while True:
            item = input("What items would you like to sell? Type \"STOP\" to stop\n")
            if item == "STOP":
                break
            price = float(input("How much does that item cost?\n"))
            stock = int(input("How many " + item + " are you selling?\n"))
            items[item] = price
            stocks[item] = stock
        self.id["restockToday"] = time.localtime()[7]
        self.id["products"] = items
        self.id["stock"] = stocks
        self.id["originalStock"] = stocks
            
        self.storeValues.write(json.dumps(self.id))
        

