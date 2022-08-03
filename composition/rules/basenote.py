from rules.rule import Rule
from chord import Chord
from progression import Progression

class BaseNote(Rule):
    def __init__(self,level):
        super().__init__()
        if (level==1):
            self.maxDistance = 2
        elif (level==2):
            self.maxDistance = 4
        else:
            self.maxDistance = 12

    #returns the possible chords that fit this rule
    def getChords(self, **kwargs):
        pass

    def ruleCheck(self, **kwargs):
        prevChord = kwargs.get("prevChord", None)
        newChord = kwargs.get("newChord", None)
        distance = abs(prevChord.stack[0]-newChord.stack[0])
        if (distance > self.maxDistance):
            return False
        return True