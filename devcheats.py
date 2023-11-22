import Levels
import Shop


def start():
    print("Enabling developer cheats...")
    PlayerStats = [9999999, 99999999, 999999, 99999, 999999]
    print(PlayerStats)
    lvl = int(input("Levels 0 to 10 or 11 for Shop >>> "))
    if lvl == 0:
        Levels.levelzero(PlayerStats)
    elif lvl == 1:
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
    elif lvl == 10:
        PlayerStats = Levels.level10(PlayerStats)
    elif lvl == 11:
        PlayerStats = Shop.shopping(PlayerStats)
    else:
        print("Going to next...")
