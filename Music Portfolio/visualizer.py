import tkinter as tk
from graphics import*
from Button import*
import threading
import random
import time
import queue
import reading_audio_data as Audio
import numpy as np
from playIt import sounders
import copy



class visualizer():

    def __init__(self, win, test, pr, path, barCount):
        self.win = win
        self.test = test
        self.path = path
        self.pr = pr
        self.rex = []
        self.barCount = barCount
        width = win.width/self.barCount
        for i in range(self.barCount):
            self.rex.append((Rectangle(Point(i*width,600),Point((i+1)*width,560)), i))
            self.rex[i][0].draw(self.win)
        
        self.isPaused = False
        self.goNow = queue.Queue()
        self.end = queue.Queue()
        self.taskComplete = threading.Event()
        self.generateFreq(path)
        self.con = True
        
    def generateFreq(self, path):
        sound = Audio.AudioData(path, self.barCount)
        self.queue = []
        for i in range(int(32*(int(len(sound.data)/sound.samplerate)))):
            self.queue.append(list(map(lambda x: self.win.height-(x*self.win.height), sound.getAverages(i, i+1))))
        self.original = copy.deepcopy(self.queue)
        
    def changeY(self):
        if self.isPaused == False:
            self.thd = threadedTask(self.goNow, self.path, self.end)
            self.thd.start()
            self.pr.changeText("Pause")
            self.count = 0
        else:
            
            self.pr.changeText("Pause")
            self.isPaused = False
            self.thd.resume.set()
            
        self.m = self.win.checkMouse()
        
        if self.goNow.get():
            
            while (self.m == None or self.test.isClicked(self.m) != True) and self.con:
                if self.m != None and self.pr.isClicked(self.m):
                    self.thd.pr.set()
                    self.isPaused = True
                    self.pr.changeText("Resume")
                    return 0
                    
                try:
                    if self.goNow.get():
                        a = self.queue[self.count]
                        self.rex = list(map(lambda x: self.theNewest(x,a), self.rex))
                        self.count += 1
                except:
                    break
                    
                self.m = self.win.checkMouse()
        self.thd.stop.set()
        self.thd.join()
        print(threading.current_thread())
        if self.con:
            self.rex = list(map(lambda x: self.theNewest(x,[560]*self.barCount), self.rex))
        self.isPaused = False
        self.pr.changeText("Play")
        self.taskComplete.set()
        #self.queue = copy.deepcopy(self.original)


    def theNewest(self, x, y):
        x[0].p2.y = y[x[1]] if y[x[1]]-10 < y[x[1]] < y[x[1]]+10 else x[0].p2.y
        
        if not x[0].canvas.isClosed():
            x[0].canvas.delete(x[0].id)
            x[0].canvas.delItem(x[0])
        x[0].canvas = None
        x[0].id = None
        x[0].canvas = self.win
        x[0].id = x[0]._draw(self.win, x[0].config)
        self.win.addItem(x[0])
        return x



        
        
class threadedTask(threading.Thread):

    def __init__(self, queue, path, end):
        super().__init__()
        self.end = end
        self.queue = queue
        self.sounds = sounders(path)
        self.pr = threading.Event()
        self.resume = threading.Event()
        self.stop = threading.Event()
        
        

    def run(self):
        c = 0
        self.sounds.playSound()
        while self.sounds.getPlayTime() <= self.sounds.getDuration():
             if(self.sounds.getPlayTime()) >= c*(1/32):
                self.queue.put(True)
                c += 1
             try:
                 if self.stop.is_set():
                    self.sounds.nssound.stop()
                    self.stop.clear()
                    
                    break
                 elif self.pr.is_set():
                     self.sounds.nssound.pause()
                     self.pr.clear()
                     self.resume.wait()
                     self.sounds.nssound.resume()
                     self.resume.clear()
                     
                     
             except:
                 print("flarbo")
                 continue

    
