from graphics import*
import tkinter as tk

'''
Dropmenu is a child class of GraphicsObject,
so in this case Dropmenu is a GraphicsObject.

Inheritance is when a child class inherits properties from a parent class,
it is used when you want to extend a class and add additional properties
from the parent class.

Heres an example of inheritance.

Say you're purchasing a car that has 4 tires, a steering wheel and 4 doors. This would be the parent class.
However there is a model of this car that has a backup camera.
This version of the car still has 4 tires, a steering wheel and 4 doors, but also has a backup camera now. This would be a child class.
It contains all the properties of it's parent class but has a new property.

'''

class Dropmenu(GraphicsObject):

    #Constructor that creates the class
    def __init__(self, win, p, start, options, com=None):
        #this calls the parent classes constructor to inherit its properties
        GraphicsObject.__init__(self,[])
        self.anchor = p.clone()
        #this creates a tkinter string variable
        self.start = tk.StringVar(win)
        self.start.set(start)
        self.options = options
        self.optionMenu = None
        self.window = win
        self.com = com
        

    
    #Getter method for current selected option in dropdown menu
    def getCurrent(self):
        choice = self.start.get()
        return choice
        

    
    #Draws Dropmenu
    def _draw(self, canvas, options):
        p = self.anchor
        x,y = canvas.toScreen(p.x,p.y)
        frm = tk.Frame(canvas.master)
        self.optionMenu = tk.OptionMenu(frm,self.start,*self.options, command=self.com)
        self.optionMenu.pack()
        self.optionMenu.focus_set()
        return canvas.create_window(x,y,window=frm)


    

        
