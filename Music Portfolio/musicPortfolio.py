from graphics import*
from Button import*
import visualizer as vis
from Dropmenu import*
import os


class MusicPortfolio():

    def __init__(self):
        self.win = GraphWin("Music Portfolio", 800, 600)
        self.play = Button(self.win, "white", "Play", Point(400,200),45)
        self.test = Button(self.win, "white", "Stop", Point(400,300),45)
        a = os.listdir(path="AudioFiles")
        self.musicSelection = Dropmenu(self.win, Point(100,100), a[0], a, self.updateSong)
        self.musicSelection.draw(self.win)
        self.vis = None

    def updateSong(self,path):
        del self.vis
        path = "AudioFiles/"+path
        self.vis = vis.visualizer(self.win, self.test, self.play, path, 100)
        


def main():
    music = MusicPortfolio()
    
    m = music.win.getMouse()
    
    while True:
        if music.play.isClicked(m):
            music.vis.changeY()

        if music.test.isClicked(m):
            print("toodles")

        

        
        m = music.win.getMouse()


if __name__ == "__main__":
    main()
