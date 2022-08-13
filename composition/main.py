#imports
from multiprocessing.sharedctypes import Value
from typing import Type
from composer import Composer
from voicing import Voicing
from progression import Progression
from chord import Chord
from rules.rule import Rule
from rules.sharedtone import SharedTone
from rules.numnotes import NumNotes
from rules.interval import Interval
from rules.firstchord import FirstChord
from rules.basenote import BaseNote
import json
from pcsets.pcset import PcSet as ps
from player import Player

# use this as a template for importing all your classes
# SharedTone rule is setup correctly, so also use that as template for structuring all other rule imports

# Goal: get this to run without errors (doesn't need to produce real results)

if __name__ == "__main__":
    with open('composition/config/config.json', 'r') as inputFile:
        ruleData = json.load(inputFile)
        melody = ruleData.get("Input").get("melody")
        key = ruleData.get("Input").get("key")
        Chord.setKey(key)
        maxRetries = ruleData.get("Settings").get("maxRetries")
        maxChords = ruleData.get("Settings").get("maxChords")
        rule2 = NumNotes(ruleData.get("NumNotes").get("priority"),ruleData.get("NumNotes").get("numNotes"))
        rule3 = SharedTone(ruleData.get("SharedTone").get("priority"),ruleData.get("SharedTone").get("numShared"))
        rule4 = Interval(ruleData.get("Interval").get("priority"),ruleData.get("Interval").get("intervals"))
        rule1 = FirstChord(ruleData.get("FirstChord").get("priority"),ruleData.get("FirstChord").get("ruleOn"))
        rule5 = BaseNote(ruleData.get("BaseNote").get("priority"),ruleData.get("BaseNote").get("level"))

    ruleList = [rule1,rule2,rule3,rule4,rule5]
    ruleList = sorted(ruleList, key=lambda rule: rule.getPriority()) #SORTS RULES

    melody = [n+12 for n in melody]
    composer = Composer(melody, ruleList, maxChords, maxRetries)
    composer.makeChordProgression()
    composer.printProgressions()
    print(len(composer.progressions),"progressions generated")
    print()
    print()
    if (len(composer.progressions) > 0):
        player = Player("composition/player.mid")
        voicer = Voicing()
        programQuit = True
        while programQuit:
            choice = input("Type 1 to hear progressions, 2 to download progressions, or 3 to end the program: ")
            print()
            if (choice == "1"):
                pressQuit = True
                while pressQuit:
                    try:
                        option = input("Choose a progression to hear or type 'q' to quit: ")
                        print()
                        if (option == 'q'):
                            pressQuit = False
                        else:
                            option = int(option)
                            progressionChosen = composer.progressions[option-1]
                            progressionIn = progressionChosen.clone()
                            melodyIn = melody[:]
                            voicer.setProgression(progressionIn)
                            voicer.setMelody(melodyIn)
                            voicer.getVoicing()
                            voicer.progression.arrChords()
                            player.writeMusic(voicer.progression, melodyIn)
                            print(voicer.progression)
                            player.playMusic()
                            
                        

                    except IndexError:
                        print("Error: Index is out of range. Please select a number from 1 to",len(composer.progressions))
                        print()
                    
                    except ValueError:
                        print()
                        print("Error: Value not recognized")
                        print()

            elif (choice == "2"):
                pass
            
            elif (choice == "3"):
                break

            else:
                print("Error: Please enter a valid input")
                print()