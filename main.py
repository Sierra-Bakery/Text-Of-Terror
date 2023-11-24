#This is a game called Text of Terror. It is a text based RPG made with the use of many modules. (inside package)
#Made by Dylan Baker at All Saints' College
#Started on 20/03/2023 Completed on 16/04/2023
#Main code for ToT consists of the main line of code that completes and calls functions/modules when needed.
#Purpose: To provide a starting place for the program,
#Also do everything that it needs to do for it to run smoothly with the other modules.
#This starts the game, asks for type of start and plays each level in correct order.
#Going to the shop after every level.
import ERRTST
import EndScreenGI
import Levels
import Shop
import sys
import time
import devcheats
import saveload
#Defining the universal variable array 'Player Stats' for use in the whole program.
PlayerStats = []
#ShpDec - Asks if the user wants to go to the shop,
#Uses the error test module to see if the user's input is good to pass through.

def ShpDec(PlayerStats):
    # Asks if the user wants to use the shop, this will add a turn to the user.
    print("""
    You feel a strange gust of wind, thinking to yourself, 'there is no wind in here'
    You look around. Off in the distance, you see an Icecream truck. Getting closer, you see the words
    ByteMerchant - Sales all over the universe!
    Do you wish to enter the shop (+1 turn) [Y/N] 
    """)
    # Validates user input before processing.
    ShpDec = ERRTST.letterinput()
    time.sleep(2)
    if ShpDec == "Y":
        print("""
        Entering the shop...""")
        time.sleep(2)
        # Adds a turn to the player
        PlayerStats[3] = PlayerStats[3] + 1
        # Sends the user to the shop module to start their shopping spree.
        Shop.shopping(PlayerStats)
        return PlayerStats
    elif ShpDec == "N":
        print("""
        You decide to pass the shop this time. The Byte Merchant disappears into a bunch of 1s and 0s.""")
        time.sleep(1)
        input("...")
        return PlayerStats
    else:
        print("INTERNAL ERROR")
#main line of code
# Defining the PlayerStats for later use in the loading of save.
PlayerStats = [0, 0, 0, 0, 0]
print(PlayerStats) # FOR DEBUG USE _ DELETE LATER _

print("""
    - - - MAKE FULL SCREEN FOR BEST EXPERIENCE - - -""")
input("""
    Press ENTER to continue...""")
print("""
    When '...' is displayed, press enter to continue.""")
time.sleep(1)
input("...")
print("""
    Nice! You got it!
    """)
time.sleep(1)
print("""




WELCOME TO...
""")
time.sleep(1)
# Displays the start screen ASCII art.
EndScreenGI.start()
time.sleep(2)
Continue = "Y"
# Asks the user if they want to play the game, if not then it exits the program.
print("""
    Do you DARE to play the TEXT OF TERRORS? (Y/N) >>> """)
# Validates user input before processing.
Open = ERRTST.letterinput()
while Continue == "Y":
    if Open == "N":
        print("Smart Choice")
        time.sleep(3)
        # Exits program because the user does not want to play.
        sys.exit()
    elif Open == "Y":
        print("Attempting to access antivirus...")
        time.sleep(2)
        # ASCII screen art for the locked out part.
        EndScreenGI.warn()
        time.sleep(2.5)
        # Asks user if they want to start new or load old save.
        print("""
    Load Save (1) or Start New Save (2) >>> """)
        # Validates user input before processing.
        gamepath = ERRTST.numberinput()
        time.sleep(1)
        if gamepath == 1:
            print("Loading last save...")
            time.sleep(1.5)
            # Loads the file 'GameState.txt' that contains the variable information for 'PlayerStats'.
            saveload.load()
            # Displays the Player's Stats.
            Continue = "N"
        elif gamepath == 2:
            print("Starting new save...")
            time.sleep(2)
            # Starts the game with level zero that assigns the player stats and gives overview and info on the game. (Tutorial)
            PlayerStats = Levels.levelzero(PlayerStats)
            # Shop function, so the player becomes familiar with what it is.
            ShpDec(PlayerStats)
            Continue = "N"
        elif gamepath == 5:
            # As the name suggests, this is for quick testing for far areas in the game. (Like a portal)
            devcheats.start()
        else:
            print("ERR_INCORRECT_INPUT")
    else:
        print("ERR_INCORRECT_INPUT")
# While the player's level does not equal 10, it will run through every iteration of levels.
while PlayerStats[4] != 10:
    lvl = PlayerStats[4]
    if lvl == 1:
        PlayerStats = Levels.level1(PlayerStats)
    elif lvl == 2:
        PlayerStats = Levels.level2(PlayerStats)
    elif lvl == 3:
        PlayerStats = Levels.level3(PlayerStats)
    elif lvl == 4:
        PlayerStats = Levels.level4(PlayerStats)
    elif lvl == 5:
        PlayerStats = Levels.level5(PlayerStats)
    elif lvl == 6:
        PlayerStats = Levels.level6(PlayerStats)
    elif lvl == 7:
        PlayerStats = Levels.level7(PlayerStats)
    elif lvl == 8:
        PlayerStats = Levels.level8(PlayerStats)
    elif lvl == 9:
        PlayerStats = Levels.level9(PlayerStats)
    elif lvl == 0:
        Levels.levelzero(PlayerStats)
    else:
        print("""
    Loading level directory error
    """)
        time.sleep(5)
    # Asks if the user wants to go to the shop.
    ShpDec(PlayerStats)
    # Asks if user wants to go fight in the arena.
    Arena(PlayerStats)
    # Deletes save file and then replaces the information with the new game state. (This is the save feature)
    saveload.murkfile()
    saveload.save(PlayerStats)
# When the player gets to level 10, they play this level.
PlayerStats = Levels.level10(PlayerStats)
print("""
Sgt. BitMonger: Well done brave soldier! Your name will go down as the greatest in all eternity! Under me ofc!
""")
# If the user survives, it will play a screen where it congratulates the player on their success.
EndScreenGI.EndGood(PlayerStats)
time.sleep(7)
# Exits the program because the user is done.
sys.exit()