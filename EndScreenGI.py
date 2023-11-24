# ScreenGraphics module made on 20/03/2023 By Dylan Baker
# Purpose: To remove clutter and these large ASCII texts from the main module.
# Further on there is a point where 2 functions open the game state file and reset all info.
import time
import sys
import saveload
#Must include variables 'waittime' and 'text' to be used in the 'LineDelayEffect' function
#Call function at the end of the text stated
#Example:
#waittime = 1
#text = """whatever
#          you want"""
#LineDelayEffect(text,waittime)

#Makes text fit to an array, that array then gets printed line by line, inbetween each line, there can be a timer set for time between each print
#This is for cascading effect
def LineDelayEffect(text, waittime):
    #When it has no time - print array and don't go through sleep cycle (remove redundancies)
    if waittime == 0:
        #Splits the lines by the {enter} character#
        lines = text
        for line in lines:
            print(line)
    #When a delay has been stated that is not zero, so it will not be instant, it will then time.sleep()
    else:
        #Splits the lines by the {enter} character
        lines = text
        for line in lines:
            print(line)
            time.sleep(waittime)

def good():
    waittime = 1
    with open("graphics.txt", 'r') as gread:
        text = gread.readlines()[0:30]
    LineDelayEffect(text, waittime)
def warn():
    waittime = 0.025
    with open("graphics.txt", 'r') as gread:
        text = gread.readlines()[31:55]
    LineDelayEffect(text, waittime)
def start():
    waittime = 0.05
    with open("graphics.txt", 'r') as gread:
        text = gread.readlines()[92:104]
    LineDelayEffect(text, waittime)
def levelart1():
    waittime = 0
    with open("graphics.txt", 'r') as gread:
        text = gread.readlines()[56:83]
        print(text)
    LineDelayEffect(text, waittime)
def fightart1():
    waittime = 0
    with open("graphics.txt", 'r') as gread:
        text = gread.readlines()[83:91]
    LineDelayEffect(text, waittime)
# Ending types
def EndBad(PlayerStats):
    print("""
    Another fallen soldier. Maybe it is time to destroy the computer.""")
    print("""
    Better luck next time! You got up to level """, PlayerStats[4])
    # Deletes all data in the file. This makes the game hardcore mode.
    saveload.murkfile()
    input("...")
    sys.exit()
def EndGood(PlayerStats):
    print("""
    Attempting to access antivirus...""")
    good()
    print("""
    Congratulations on your great work, fine soldier!""")
    print("""
    Your Player Stats are: Health, """, PlayerStats[0], "ect.....")
    # Deletes all data in the file. This makes the game hardcore mode.
    saveload.murkfile()
    input("...")
    time.sleep(4)
    # Stops the game as the user is finished. There is nothing more, nothing less.
    print("Bye! :) Thanks for playing")

    sys.exit()