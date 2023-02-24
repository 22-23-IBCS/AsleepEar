from graphics import*
from Button import*
from scrollBox import*
import visualizer as vis
from Dropmenu import*
import os
import time


class MusicPortfolio():

    def __init__(self):
        self.win = GraphWin("Music Portfolio", 800, 600)
        self.play = Button(self.win, "white", "Play", Point(350,480),45)
        self.test = Button(self.win, "white", "Stop", Point(450,480),45)
        self.updateBio = Button(self.win, "white", "Update\nBio", Point(100,140),45)
        self.loading = Text(Point(400,440), "Loading Audio, Please Wait...")
        a = [i[:len(i)-4] for i in os.listdir(path="AudioFiles") if i[len(i)-4:] == ".wav"]
        temp = ""
        if not os.path.exists("aboutMe.txt"):
            holdOn = open("aboutMe.txt", "w")
            holdOn.write("Write Bio Here")
            holdOn.close()
        with open("aboutMe.txt", "r") as j:
            temp = j.read()
            
        self.covers = {}
        for i in range(len(a)):
            self.covers[a[i].split("_")[1]] = a[i].split("_")[0]
            a[i] = a[i].split("_")[1]
            
        
         
        self.bio = scrollBox(self.win, Point(100,300), 20,20, True)
        self.bio.draw(self.win)
        self.bio.setText(temp)
        self.musicSelection = Dropmenu(self.win, Point(400,50), a[0], a, self.updateSong)
        self.musicSelection.draw(self.win)
        self.vis = None
        self.updateSong(a[0])

    def updateSong(self,path):
        
        if self.vis != None:
            self.vis.con = False
            for i in self.vis.rex:
                i[0].undraw()
            del self.vis
            self.albumPic.undraw()
            
        
        self.albumPic = Image(Point(400,250), "AlbumCovers/"+self.covers[path]+".png")
        self.albumPic.draw(self.win)
        path = "AudioFiles/"+self.covers[path]+"_"+path+".wav"
        self.loading.draw(self.win)
        self.vis = vis.visualizer(self.win, self.test, self.play, path, 100)
        self.loading.undraw()
        


def main():
    
    music = MusicPortfolio()
    
        
    m = music.win.getMouse()
    
    while True:
        if music.play.isClicked(m):
            music.vis.changeY()

        if music.test.isClicked(m):
            print("toodles")

        if music.updateBio.isClicked(m):
            with open("aboutMe.txt", "w") as j:
                j.write(music.bio.getText())

        

        
        m = music.win.getMouse()


if __name__ == "__main__":
    main()
