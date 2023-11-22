# Save and Load Module made on 15/04/2023 By Dylan Baker
# Purpose: To save the important Player Stats.
# So the program can be closed and resume at a later time and no progress is lost.
# Using eval function when loading information, this is untrustworthy
# Since this only used in this one way, it's downsides are admissible.
import os
import Levels


def save(PlayerStats):
    print("""
    Saving...
    """)
    # Openes the file and engages the write function. Then uses the variable Player Stats to write to the file.
    with open('GameState.txt', 'w') as GS:
        GS.write(str(PlayerStats))
        # Closes the file for it to not be in the way for other program.
        GS.close()
    print("""
    Saved!
    """)
def load():
    print("Loading Last Save...")
    # Checks if there is a file called GameState in the operating folder, if not then it will tell the user to make one.
    # Checks if there is any data in file, if there is none then it will start a new save.
    # Opens the file and engages the read function.
    # Then finds the numbers inside the file and assigns them to the array Player Stats.
    # NOTE: IT IS THE ONLY THING IN IT
    try:
        if os.path.isfile('GameState.txt'):
            if os.path.getsize('GameState.txt') > 0:
                with open('GameState.txt', 'r') as f:
                    PlayerStats = eval(f.read())
                    print("Loaded!")
                    print("Loaded Player Stats as: Health -> ", PlayerStats[0], " | Cash -> ", PlayerStats[1], " | Kills -> ", PlayerStats[2], " | Turns -> ", PlayerStats[3], " | Level -> ", PlayerStats[4])
                    return PlayerStats
            else:
                print("No data in file, starting new save!")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("| CRITICAL ERROR | File not found! Please create a file called GameState.txt in the game folder!")
    except Exception as e:
        print(f"An error occurred: {e}")
def murkfile():
    # Openes the file and engages the write function.
    # Then deletes all data inside the file in order to stop retrying of levels. Very mean. I know... :)
    with open('GameState.txt', 'w') as GS:
        GS.write('')
        GS.close()
        # Closes the file for it to not be in the way for other program.