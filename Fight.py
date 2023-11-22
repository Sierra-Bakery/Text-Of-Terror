#Fight module made on 23/03/2023 By Dylan Baker
#Purpose: To handle all the fighting mechanics. Determine a winner or loser in fight.
import ERRTST
import EndScreenGI
import Hostile
import random
import time

def PlrToHstl(EnemyStats, EnemyType, PlayerStats):
	# Asks for attack and gives info on it
	print("""	You must choose what attack do you want to use:
	[1] System Restart:	D10, Roll > 4 to hit.	Risk - MED	| Damage - MED
	[2] Task Manager:	D10, Roll > 2 to hit.	Risk - LOW	| Damage - LOW
	[3] Go Offline:		D5, Roll > 2 to hit.	Risk - MED	| Damage - HIGH
	[4] Scan Hardware:	D20, Roll > 10 to hit.	Risk - HIGH | Damage - HIGH
	""")
	# Validates user input before processing
	WhtAttk = ERRTST.numberinput()
	# Different attacks have changing chances for getting a crit hit or missing and damage levels.
	# Due to many instances of this, it will only be stated once.
	# Depending on the attack choice, random number is given and that influences the power of attack.
	if WhtAttk == 1:
		print("You decide to restart the system with 'shutdown -r' The prompt on the screen shows 'Restarting computer, this might take a while'...")
		roll = random.randint(1,10)
		print("Restarting the computer had an effect of ", roll)
		if roll > 8:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 100
			print("Critical Hit! You dealt 100 damage against the ", EnemyType)
		elif roll >= 5:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 50
			print("You dealt 50 damage against the ", EnemyType)
		else:
			# Takes health from the enemy and gives attack info
			print("That sucks, you missed your attack!")
		input("Press Enter to Continue...")
	elif WhtAttk == 2:
		print("You open task manager, after searching for a while for the ", EnemyType, ", you find it and quickly end task...")
		roll = random.randint(1,10)
		print("Task manager is not responding... but it could still be working... you rolled a ", roll)
		if roll > 8:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 75
			print("Critical Hit! You dealt 75 damage against the ", EnemyType)
		elif roll > 5:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 50
			print("You dealt 50 damage against the ", EnemyType)
		elif roll > 2:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 25
			print("You dealt 25 damage against the ", EnemyType)
		else:
			# Takes health from the enemy and gives attack info
			print("This attack had no effect at all... better try something else :(")
		input("Press Enter to Continue...")
	elif WhtAttk == 3:
		print("You unplug the ethernet cable behind your computer. Google stops working, hope that the ", EnemyType, " needs internet to work!...")
		roll = random.randint(1,5)
		print("It has been a while since you turned the internet on, your crave for cat videos is too great, you plug it back in and watch. You rolled a ", roll)
		if roll == 5:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 200
			print("Critical Hit! You dealt 200 damage against the ", EnemyType)
		elif roll > 2:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 25
			print("You dealt 25 damage against the ", EnemyType)
		else:
			# Takes health from the enemy and gives attack info
			print("The ", EnemyType, " laughs in binary. Your attack had no effect.")
		input("Press Enter to Continue...")
	else:
		print("You open windows antivirus, apart from being very simple, it gets the job done. Sometimes, that is.")
		roll = random.randint(1,20)
		print("You activate the program, the screen flickers a bit, maybe from the intense battle occurring inside the computer? At-least hope that it is. You rolled a ", roll)
		if roll > 18:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 500
			print("Critical Hit! You dealt 500 damage against the ", EnemyType)
		elif roll > 10:
			# Takes health from the enemy and gives attack info
			EnemyStats[0] = EnemyStats[0] - 25
			print("You dealt 25 damage against the ", EnemyType)
		else:
			# Takes health from the enemy and gives attack info
			print("You took the risk, it failed, but dont fret, there is always a next time! Your attack had no effect.")
		input("Press Enter to Continue...")
	return PlayerStats and EnemyStats
def HstlToPlr(EnemyType, PlayerStats):
	print("The ", EnemyType, "'s raging hatred towards everything uninfected is too great, it is looking at you suspiciously :O, in binary of course! 001010010")
	#Generates a number that will be the power of the enemy's attack, this is then assigned to the roll variable
	roll = random.randint(1,25)
	print("How bad can a ", EnemyType, " be? Depends on it's dice roll right? Wrong! Not the roll bit, but the dice. This game has no dice! XD | Enemy rolled ", roll)
	if roll == 25:
		print("Oh No!")
		time.sleep(1)
		print("""CRITICAL HIT!
		Hope you survive this""")
		# Takes health from the player and gives attack info
		enemydmg = random.randint(100,151)
		PlayerStats[0] = PlayerStats[0] - enemydmg
		print(EnemyType, " Hit you with ", enemydmg, " damage!")
	elif roll >= 20:
		# Takes health from the player and gives attack info
		enemydmg = random.randint(75, 100)
		PlayerStats[0] = PlayerStats[0] - enemydmg
		print("You just escaped the full force of the attack, but still got hit in the process. ", enemydmg, " Damage.")
	elif roll >= 10:
		# Takes health from the player and gives attack info
		enemydmg = random.randint(50, 75)
		PlayerStats[0] = PlayerStats[0] - enemydmg
		print("The ", EnemyType, " is somehow tired and only hit you with 25% of max power. ", enemydmg, " Damage.")
	elif roll > 5:
		# Takes health from the player and gives attack info
		enemydmg = random.randint(1,20)
		PlayerStats[0] = PlayerStats[0] - enemydmg
		print("The attacker is not very good, it only shutdown some of your sub-processes, minor inconvenience. ", enemydmg, " Damage.")
	else:
		# Gives attack info
		print(EnemyType, " had a major glitch that caused it to miss you completely! No damage.")
	return PlayerStats
def fight(PlayerStats):
	print("As you scour the binary code in front of you, you see a strange combination, you look further to investigate...")
	# Tells the player their stats
	print("You have ", PlayerStats[0], "HP.")
	# Determines the Type of enemy and their stats. To be used later on in the fight. Found by the player level.
	EnemyType = Hostile.HostileSlct(PlayerStats)
	EnemyStats = Hostile.HostileStats(EnemyType)
	print("You (somehow) stumble into a fight with an odd line of code. How you fight code, no one knows.")
	print("You are fighting a ", EnemyType, " with ", EnemyStats[0], " health!")
	print("You decide to load a fight program...")
	print("Fight.exe: Attack mode engaging...")
	input("Press Enter to Continue...")
	# Random numbers for visual effect
	comple = random.randint(40,60)
	print(comple, "% loaded...")
	comple = random.randint(60,99)
	time.sleep(1.5)
	print(comple, "% loaded...")
	time.sleep(0.5)
	print("Fight.exe: Fight mode engaged! TARGET ACQUIRED")
	time.sleep(1)
	go = "Y"
	# Shows ASCII art of the word FIGHT!
	EndScreenGI.fightart1()
	time.sleep(3)
	while go == "Y":
		# Displays general player stat info
		print("Your Health -> ", PlayerStats[0], " | Enemy Name -> ", EnemyType, " | Enemy Health -> ", EnemyStats[0])
		print("Prepare to rain hell on your enemy! | Your turn!")
		# Runs the Player fighting against hostile function, this effects the hostile only.
		PlrToHstl(EnemyStats, EnemyType, PlayerStats)
		# Adds a turn to the user, as they did something.
		PlayerStats[3] = PlayerStats[3] + 1
		# If the health of the enemy is over 0, has any left, it will run a hostile to player attack.
		if EnemyStats[0] > 0:
			# Runs the hostile to player attack, this effects the player's stats only
			HstlToPlr(EnemyType, PlayerStats)
			# If the player still has health then it will do the player to hostile function again.
			if PlayerStats[0] > 0:
				time.sleep(0.5)
				input("Press Enter to Continue...")
				print("Fight.exe: You survived the attack, congrats!")
				go = "Y"
			else:
				time.sleep(2)
				input("Press Enter to Continue...")
				print("Fight.exe: You died!")
				# Since player has died, has no health left, Displays the ending screen to the game.
				EndScreenGI.EndBad(PlayerStats)
				go = "N"
		else:
			print("Fight.exe: Congratulations! You somehow defeated a computer program!")
			time.sleep(0.5)
			print("           Fight finished. Shutting down...")
			time.sleep(1)
			# Defeated enemy and now is given the rewards for defeat, which is the second value in the hostile stats array.
			PlayerStats[1] = PlayerStats[1] + EnemyStats[1]
			go = "N"
	# Displays player stats.
	print("Your Health -> ", PlayerStats[0], " | Cash -> ",  PlayerStats[1], " | Kills -> ", PlayerStats[2], " | Turns -> ", PlayerStats[3])
	return PlayerStats