#Hostile module made on 20/03/2023 By Dylan Baker
#Purpose: To find an enemy type and assign it values; health, cash.
#To find player level and find a suitable enemy. Would not have endgame enemy vs new player and vice versa.
import random

def HostileSlct(PlayerStats):
    # If the level of the user is in range, a certain name will be assigned.
    if PlayerStats[4] <= 3:
        hstlroll = random.randint(1,2)
        if hstlroll == 1:
            EnemyType = "Bug"
        else:
            EnemyType = "Virus"
    elif PlayerStats[4] <= 6:
        hstlroll = random.randint(1,3)
        if hstlroll == 1:
            EnemyType = "Bug"
        elif hstlroll == 2:
            EnemyType = "Virus"
        else:
            EnemyType = "Malware"
    elif PlayerStats[4] <= 9:
        hstlroll = random.randint(1,3)
        if hstlroll == 1:
            EnemyType = "Virus"
        elif hstlroll == 2:
            EnemyType = "Malware"
        else:
            EnemyType = "Trojan"
    else:
        EnemyType = "MEMZ.exe"
    return EnemyType
def HostileStats(EnemyType):
    # Depending on the name, the values health and reward for kill is given.
    if EnemyType == "Bug":
        EnemyStats = [100, 20]
    elif EnemyType == "Virus":
        EnemyStats = [250, 50]
    elif EnemyType == "Malware":
        EnemyStats = [500, 100]
    elif EnemyType == "Trojan":
        EnemyStats = [750, 250]
    elif EnemyType == "MEMZ.exe":
        EnemyStats = [2000, 1000]
    return EnemyStats