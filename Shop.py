#Shop module made on 19/03/2023 By Dylan Baker
#Purpose: Game shop, this is where the user can buy health or buy spins on the fortune wheel.
#Shop does not allow the user to buy something that they cannot afford.
#In health Shop, answer "5", +999999 Health+Money | FOR TEST USE | - DELETE LATER - | Or will I?.. (Perfect easter egg)
import random
import time
import ERRTST

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
        shopping(PlayerStats)
        return PlayerStats
    elif ShpDec == "N":
        print("""
        You decide to pass the shop this time. The Byte Merchant disappears into a bunch of 1s and 0s.""")
        time.sleep(1)
        input("...")
        return PlayerStats
    else:
        print("INTERNAL ERROR")

def shopping(PlayerStats):
    # Starts shopping variable to engage the while loop, so there is a choice to keep shopping.
    shopping = "Y"
    while shopping == "Y":
        # Informs the user of their stats to decide what to buy or not.
        print("Your Player Stats: Health -> ", PlayerStats[0], " | Cash -> ", PlayerStats[1], " | Kills -> ", PlayerStats[2], " | Turns -> ", PlayerStats[3], " | Level -> ", PlayerStats[4])
        time.sleep(2)
        # Asks where to go
        print("""
        Byte Merchant: Welcome to the inter-computing shop, here for all your needs!
        Would you like to shop for health [1] or try your luck at the fortune wheel? [2]
        Or Stop shopping [3]
        """)
        # Validates response before processing
        shopnum = ERRTST.numberinput()
        time.sleep(1)
        if shopnum == 1:
            #Asks what size of health the user wants to buy
            print("""
            Byte Merchant: Welcome to the Health Shop!
            Here we sell Health of all sizes,
            [1] 50hp - $25
            [2] 100hp - $45
            [3] 500hp - $400""")
            # Validates response before processing
            buyc = ERRTST.numberinput()
            time.sleep(1)
            if buyc == 1:
                print("Buying +50 HP for $25")
                time.sleep(2)
                # Checks is the user can afford the purchase, if so then deducts the money and adds the health.
                if PlayerStats[1] >= 25:
                    PlayerStats[1] = PlayerStats[1] - 25
                    PlayerStats[0] = PlayerStats[0] + 50
                else:
                    print("Sorry, you cannot afford this.")
                    time.sleep(2)
            elif buyc == 2:
                print("Buying +100 HP for $45")
                time.sleep(2)
                # Checks is the user can afford the purchase, if so then deducts the money and adds the health.
                if PlayerStats[1] >= 45:
                    PlayerStats[1] = PlayerStats[1] - 45
                    PlayerStats[0] = PlayerStats[0] + 100
                else:
                    print("Sorry, you cannot afford this.")
                    time.sleep(2)
            elif buyc == 3:
                print("Buying +500 HP for $400")
                time.sleep(2)
                # Checks is the user can afford the purchase, if so then deducts the money and adds the health.
                if PlayerStats[1] >= 400:
                    PlayerStats[1] = PlayerStats[1] - 400
                    PlayerStats[0] = PlayerStats[0] + 500
                else:
                    print("Sorry, you cannot afford this.")
                    time.sleep(2)
            elif buyc == 5:
                # This is purely for development use, when testing the game this was used to see if all aspects worked.
                print("HAHA nice dev cheats...")
                PlayerStats[0] = PlayerStats[0] + 999999
                PlayerStats[1] = PlayerStats[1] + 999999
                print("Here, have some Health and Money. It's on the house!")
            else:
                print("Sorry, incorrect input.")
                time.sleep(2)
        elif shopnum == 2:
            print("You have $", PlayerStats[1])
            print("""Byte Merchant: Would you like to try your luck on the wheel of fortune?
            Each spin costs $75""")
            # Validates user input before processing
            wlspin = ERRTST.letterinput()
            time.sleep(1)
            while wlspin == "Y":
                #If money is more than the cost, then allow to spin wheel
                if PlayerStats[1] > 75:
                    print("Spinning the wheel...")
                    print("    -$75")
                    # Deducts funds to spin wheel
                    PlayerStats[1] = PlayerStats[1] - 75
                    time.sleep(1)
                    # Displays random numbers for the sense of the wheel spinning
                    print(random.randint(1,50))
                    time.sleep(1)
                    print(random.randint(1,50))
                    time.sleep(1)
                    print(random.randint(1,50))
                    time.sleep(1)
                    print(random.randint(1,50))
                    time.sleep(2)
                    print(random.randint(1,50))
                    time.sleep(3)
                    # Finally selects a number to use as the wheel roll.
                    wheelroll = random.randint(1, 50)
                    print("The wheel landed on -> ", wheelroll)
                    # Depending on the number, different prises can be won.
                    if wheelroll == 50:
                        print("JACKPOT!!! YOU WON $1000")
                        time.sleep(3)
                        # Gives Cash to the user
                        PlayerStats[1] = PlayerStats[1] + 1000
                    elif wheelroll <= 49 and wheelroll >= 45:
                        print("Congratulations, you won 500 HP")
                        time.sleep(3)
                        # Gives Health to the user
                        PlayerStats[0] = PlayerStats[0] + 500
                    elif wheelroll <= 44 and wheelroll >= 40:
                        print("Congratulations, you won 250 HP")
                        time.sleep(3)
                        # Gives Health to the user
                        PlayerStats[0] = PlayerStats[0] + 250
                    elif wheelroll <= 39 and wheelroll >= 30:
                        print("Congratulations, you won $100 HP")
                        time.sleep(3)
                        # Gives Cash to the user
                        PlayerStats[1] = PlayerStats[1] + 100
                    elif wheelroll <= 29 and wheelroll >= 20:
                        print("Congratulations, you won 50 HP")
                        time.sleep(3)
                        # Gives Health to the user
                        PlayerStats[0] = PlayerStats[0] + 50
                    elif wheelroll <= 19:
                        # Lost so nothing is given to the user
                        print("Uh oh! You lost :( Better luck next time!")
                        time.sleep(3)
                    else:
                        print("ERR_WHEEL-ROLL_NOT_VALID")
                    wlspin = "N"
                else:
                    print("Sorry, you cannot afford this.")
                    time.sleep(2)
            print("Exiting wheel of fortune...")
            time.sleep(2)
        elif shopnum == 3:
            shopping = "N"
        else:
            print("ERR_INCORRECT_INPUT")
    print("""
    Exiting Shop...
    """)
    return PlayerStats