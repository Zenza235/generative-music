#importing pitch class set module (pcsets)
import pcsets as ps
from pcsets import pcset
import rules

class interval(rules):
    
    def __init__(self, intervalLengths):
        self.intintervalLengths = intervalLengths
    
    def getChords(self):
        pass
    #finds the notes one interval distance above the current note with all the possible interval lengths
    def intUp(intervalLength,note):
        pass

    #finds the notes one interval distance below the current note with all the possible interval lengths
    def intDown(intervalLength,note):
        pass
