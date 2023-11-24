#Arena for fights that are not in the normal story line
#Made to have more things happening in the game.
#By Dylan Baker @ 24/11/2023
import ERRTST
import ScreenGraphics
def ArenaDec(PlayerStats):
    print("""
    You hear a loud zap, a door openes infront of you. The cries of programs radiating from the entrance.
    Do you enter?
""")
    GoIn = ERRTST.letterinput()
    if GoIn == "Y":
        ScreenGraphics.EnterArena()
        MainArena(PlayerStats)
        return PlayerStats
    else:
        print("Too scary i guess...")
        return PlayerStats
def MainArena(PlayerStats):
    print("Welcome to main arena!")