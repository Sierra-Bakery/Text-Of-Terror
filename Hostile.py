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
        c = random.randint(20,50)
        EnemyStats = [100, c]
    elif EnemyType == "Virus":
        c = random.randint(50,100)
        EnemyStats = [250, c]
    elif EnemyType == "Malware":
        c = random.randint(100,150)
        EnemyStats = [500, c]
    elif EnemyType == "Trojan":
        c = random.randint(250,350)
        EnemyStats = [750, c]
    elif EnemyType == "MEMZ.exe":
        c = random.randint(1000,2500)
        EnemyStats = [2000, c]
    return EnemyStats