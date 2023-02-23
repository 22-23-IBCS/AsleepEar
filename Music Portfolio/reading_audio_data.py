from scipy.io import wavfile
import numpy as np
import time
class AudioData():

    def __init__(self, audioFile, barcount):
        self.ready = False
        self.barCount = barcount
        self.samplerate, self.data = wavfile.read(audioFile)
        self.data = self.data if len(self.data.shape) == 1 else self.data[:,1]
        self.inter = int(self.samplerate*(1/32))
        z = np.abs(np.fft.fftn(self.data, norm="forward"))
        self.norm = max(z)
        self.ready = True

    def getNorm(self):
        return self.norm

    def getAverages(self, fro, to):
        ranges = []
        rab = []
        try:
            yf = np.fft.fftn(self.data[self.inter*fro:self.inter*to], norm="forward")
            yf = yf[int((1/self.barCount)*len(yf)):int((self.barCount-1/self.barCount)*len(yf))]
        except ValueError:
            print(self.data[self.inter*fro:self.inter*to])
            print(fro)
            print(to)
            print(len(self.data))
        inter = int(len(yf)/self.barCount)
        
        for i in range(self.barCount):
            t = np.abs(yf[inter*i:inter*(i+1)])
            hold = (sum(t)/inter)/self.norm
            temp = hold if hold <= 1 else np.sqrt(hold)/hold
            ranges.append(hold)
        
        return ranges
