import DefaultStore as ds
import json
import time

class GroceryStore(ds.store):

    def __init__(self):
        super().__init__()
        self.restock()
        self.func = {"getItems" : self.getItems, "talkToManager" : self.talkToManager, "purchaseItems" : self.purchaseItems}
        

    def restock(self):
        if time.localtime()[7] != self.id["restockToday"]:
            self.id["restockToday"] = time.localtime()[7]
            print("IT'S RESTOCKING TIME!!!!!\n")
            print("Before Restock:")
            self.getItems()
            for i in self.id["originalStock"].keys():
                self.id["stock"][i] = self.id["originalStock"][i]
            
                
            print("After Restock:")
            self.getItems()
        
        
    def getItems(self):
        
        print("---------------------")
        for i in self.id["stock"].keys():
            print(i + ": " + str(self.id["products"][i]) + " " + "(Stock: " + str(self.id["stock"][i]) + ")")

        print("---------------------")

    def talkToManager(self):
        complaint = input("fine.. what would you like to say")
        print("Hello I'm the manager " + self.id["manager"] + ". I'm sorry that " + complaint + " I will be sure this doesn't happen again")

    def purchaseItems(self):
        print("What would you like to purchase?\nWe sell:\n")
        self.getItems()
        items = []
        price = 0
        
        while True:
            print("What would you like to purchase? Type \"STOP\" to stop")
            user = input()
            if user == "STOP":
                break
            if user in self.id["products"] and self.id["stock"][user] != 0:
                howMany = int(input("How many items would you like to purchase?\n"))
                if howMany <= self.id["stock"][user]:
                    self.id["stock"][user] -= howMany
                    items.append(user)
                    price += (howMany*self.id["products"][user])
                else:
                    print("We don't have that in stock, please try again")
                    continue
            else:
                print("That item does not exist")
                continue
        print("You bought:\n")
        for i in items:
            print(i)
        print("Subtotal: " + str(price))
        print("Tax: " + str(price*self.id["salesTax"]))
        print("Total: " + str(price+(price*self.id["salesTax"])))


def main():
    store = GroceryStore()
    print("Hello! Welcome To " + store.id["storeName"] + "!")
    print("Your " + store.id["storeName"] + " manager is " + store.id["manager"] + ".")
    print("We restock once every day.\n")

    while True:
        
        print("What would you like to do? Type \"STOP\" to stop")
    
        user = input("getItems, talkToManager, or purchaseItems\n")
        if (user == "STOP"):
            break
        store.func[user]()
    
    
    open("Store Info.json", "w").write(json.dumps(store.id))
    
    
    


if __name__ == "__main__":
    main()



