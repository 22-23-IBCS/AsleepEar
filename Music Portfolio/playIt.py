from graphics import*
from Button import*
import threading
from playsound import playsound
import tkinter as tk

class sounders():

    def __init__(self, path):
        self.setUpSong(path)

    def getPlayTime(self):
        return self.nssound.currentTime()

    def getDuration(self):
        return self.nssound.duration()

    def playSound(self):
        self.nssound.play()
        
    def _canonicalizePath(self, path):
        """
        Support passing in a pathlib.Path-like object by converting to str.
        """
        import sys
        if sys.version_info[0] >= 3:
            return str(path)
        else:
            # On earlier Python versions, str is a byte string, so attempting to
            # convert a unicode string to str will fail. Leave it alone in this case.
            return path

    def _handlePathOSX(self, sound):
        sound = self._canonicalizePath(sound)

        if '://' not in sound:
            if not sound.startswith('/'):
                from os import getcwd
                sound = getcwd() + '/' + sound
            sound = 'file://' + sound

        try:
            # Don't double-encode it.
            sound.encode('ascii')
            return sound.replace(' ', '%20')
        except UnicodeEncodeError:
            try:
                from urllib.parse import quote  # Try the Python 3 import first...
            except ImportError:
                from urllib import quote  # Try using the Python 2 import before giving up entirely...

            parts = sound.split('://', 1)
            return parts[0] + '://' + quote(parts[1].encode('utf-8')).replace(' ', '%20')

    def setUpSong(self, path):
        sound = path
        block = True
        try:
            from AppKit import NSSound
        except ImportError:
            logger.warning("playsound could not find a copy of AppKit - falling back to using macOS's system copy.")
            sys.path.append('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC')
            from AppKit import NSSound

        from Foundation import NSURL
        from time       import sleep

        sound = self._handlePathOSX(sound)
        url = NSURL.URLWithString_(sound)
        if not url:
            raise PlaysoundException('Cannot find a sound with filename: ' + sound)

        for i in range(5):
            self.nssound = NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
            if self.nssound:
                break
            else:
                logger.debug('Failed to load sound, although url was good... ' + sound)
        else:
            raise PlaysoundException('Could not load sound with filename, although URL was good... ' + sound)

