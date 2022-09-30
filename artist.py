import turtle
import math

class Artist():

    def __init__(self):
        self.canvas = turtle.Screen()
        self.canvas.title("window")
        self.t = turtle.Turtle()
        


    def go(self,x,y):
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()
        

    def triangle(self, size = 100,x=100,y=100):
        t = self.t
        self.go(x,y)
        for i in range(3):
            t.right(120)
            t.forward(size)


    def square(self,size=100, x=-100,y=100):
        t = self.t
        self.go(x,y)
        for i in range(4):
            t.forward(size)
            t.right(90)
        

    def circle(self, size=100, x=0,y=0):
        t = self.t
        self.go(x,y)
        t.seth(0)
        size /= 2
        t.forward(size)
        distance = math.sqrt(pow((size-(size*math.cos((math.pi)/180))),2)+pow((-(size*math.sin((math.pi)/180))),2))
        t.left(90)

        
        for i in range(360):
            t.forward(distance)
            t.left(1)

    
    def star(self, size=100, x=100, y=-100):
        t = self.t
        self.go(x,y)
        for i in range(6):
            t.left(216)
            t.forward(size)


    def specialStar(self,x= 100, y = 50):
        size = 50
        t = self.t
        self.go(x,y)
        t.seth(0)
        
        for i in range(6):
            t.forward(size)
            t.left(72)
            t.forward(size)
            t.right(144)
        

    def ellipse(self, a=3,b=4, x=0,y=0):
        t = self.t
        self.go(x,y)
        t.seth(0)
        t.forward(a)
        t.seth(90)
        for i in range(1,361):
            #print(t.pos()[0])
            t.forward(math.sqrt(pow(((a*math.cos(((i-1)*math.pi)/180))-(a*math.cos((i*math.pi)/180))),2)+pow((b*math.sin(((i-1)*math.pi)/180)-(b*math.sin((i*math.pi)/180))),2)))
            t.left(1)

        
        
        
        
            


    def polygon(self,size=100, sides=5, x=-100,y=-100):
        t = self.t
        self.go(x,y)
        angle = 360/sides
        t.seth(angle)
        size = self.sideLength(size, sides)
        for i in range(sides):
            t.forward(size)
            t.right(angle)


    def smileyFace(self,x=100,y=100):
        t = self.t

        self.go(x,y)
        t.seth(270)
        t.circle(50, 180)
        self.go(x+25,y+50)
        t.seth(90)
        t.forward(25)
        self.go(x+75,y+50)
        t.forward(25)
        self.go(0,0)


    
    def sideLength(self, size, sides):
        iAngle = ((sides-2)*180)/sides
        dAngle = iAngle/(sides-2)
        if sides%2 == 0:
            return ((size*math.sin((dAngle*math.pi)/180))/math.sin(((180-(iAngle/2)-dAngle)*math.pi)/180))
        else:
            dAngle /= 2
            return (size*math.tan((dAngle*math.pi)/180))*2
            

    
        
        
        
    

def main():
    start = Artist()
    start.triangle()
    start.t.clear()
    start.circle()
    start.t.clear()
    start.square()
    start.t.clear()
    start.star()
    start.t.clear()
    start.t.polygon(100,8)
    start.t.clear()
    start.ellipse(50,25)
    start.t.clear()
    start.t.smileyFace()
    
    
    


if __name__ == "__main__":
    main()
