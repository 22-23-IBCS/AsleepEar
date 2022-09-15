class Dog:
    def __init__ (self, breed, color, barkSound, hungry, name):
        self.breed = breed
        self.color = color
        self.sound = barkSound
        self.hungry = hungry
        self.name = name

    def isHungry(self):
        if(self.hungry):
            print(self.name + " is hungry")
        else:
            print(self.name + " is not hungry")
        return self.hungry

    def eat(self):
        self.hungry = False
        print("Monch")

    def getName(self):
        return self.name



    
    

def main():

    dog1 = Dog("Golden Retriever", "Golden",  "woof", True, "Flash")
    dog2 = Dog("Labradoodle", "Black", "bark", False, "Percy")

    print("Name of dog 1: " + dog1.getName())
    print("Name of dog 2: " + dog2.getName())

    print()

    dog1.isHungry()
    dog1.eat()
    dog1.isHungry()
    



if __name__ == "__main__":
    main()
