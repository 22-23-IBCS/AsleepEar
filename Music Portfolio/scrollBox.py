from graphics import*
import tkinter as tk




class scrollBox(GraphicsObject):

    #Constructor for the scrollBox object
    def __init__(self, win, p, w, l, hasBorder):
        GraphicsObject.__init__(self,[])
        self.anchor = p.clone()
        self.width = w
        self.length = l
        self.hasBorder = hasBorder
        
    #Returns the values in the text box
    def getText(self):
        return self.entryPoint.get("1.0", 'end-1c')

    #Sets text in text box
    def setText(self, value):
        self.entryPoint.delete("1.0","end")
        self.entryPoint.insert("1.0",value)
        
     
        
    #Draws the scrollBox object as well as instantiates the values for the text box and scroll bars
    def _draw(self, canvas, heha):
        p = self.anchor
        x,y = canvas.toScreen(p.x,p.y)
        frm = tk.Frame(canvas.master)
        self.entryPoint = tk.Text(frm,width=self.width,height=self.length, wrap="word", bg="#cccccc")
        self.entryPoint.insert("0.0", "Enter Text")
        self.textVsb = tk.Scrollbar(frm, orient="vertical", command=self.entryPoint.yview)
        self.entryPoint.configure(yscrollcommand=self.textVsb.set)
        self.textVsb.pack(side="left",fill="y")
        self.textVsb.focus_set()
        self.entryPoint.pack()
        self.entryPoint.focus_set()
        return canvas.create_window(x,y,window=frm)


        

        


        
        
        
