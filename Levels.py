#Level module made on 23/03/23 by Dylan Baker
#Purpose: This is where the storyline is stored. This is made into module to cull clutter.
#The first level is to determine values of variables and start the game (With introduction).
#All other levels are for storyline and towards completion of the game.
#This module does not provide any real change in variables or contains code other than print and module calling.
#Due to this, there is very little to describe about what is going on.
#Functions for all levels. This is so individual level can be called when concurrent with the playerstats[4]
import random

import Fight
import time
import EndScreenGI
import saveload

def levelzero(PlayerStats):
	print("""
	Text of Terrors is a text based Semi-RPG, where you make choices on certain things and other times hope for the best.
	Make the most of your surroundings, use the shop to replenish your health.
	Or, win it big ong the wheel!
	Now we start the adventure...
	""")
	input("...")
	health = random.randint(250,500)
	cash = 0
	kills = 0
	turns = 0
	level = 0
	PlayerStats = [health, cash, kills, turns, level]
	print(PlayerStats)
	print("""
	
	You start with """, PlayerStats[0], """ health!
	
	""")
	saveload.save(PlayerStats)
	input("...")
	print("""
	Welcome to hell rookie!
	I am Sergeant BitMonger, commander of the ANTI-MW sector of bit-fighters battalion.
	Over here, there is nothing but pain and suffering. It is a real battle field out there. Truly kill or be killed.
	You probably don't even know what i am talking about...
	Well, i am going to keep it a dime with you...
	We have a problem, and you are here to fix it for us...""")
	input("...")
	print("""
	Sgt. BitMonger: So what do you say, you in?...""")
	input("...")
	print("""
	Not one to talk? That is okay, you didn't really have a choice anyways.
	Let's get to it then...""")
	input("...")
	print("""
	We will be converting you into binary and injecting you into the USB port of a computer.
	This has only been done once before, but sadly our soldier was infected by the hostiles.
	Be careful in there. There are many hostile programs that are ravaging the computer as we speak.
	It is your job to destroy them by getting to the antivirus and activating it.
	Hopefully destroying these spiteful creatures.
	Good luck brave soldier!
	Nurse Yranib! Your turn.""")
	input("...")
	print("""
	Nurse Yranib: Okay sweetie, we will now download your consciousness to the transfer program...""")
	time.sleep(4)
	print("01010111 01000001 01001011 01000101 00100000 01010101 01010000 00001010")
	time.sleep(0.2)
	print("01000100 01001111 01001110 00100111 01010100 00100000 01000111 01001111 00001010")
	time.sleep(0.2)
	print("01010011 01110101 01000110 01100110 01100101 01110010")
	time.sleep(0.2)
	print("01010111 01000001 01001011 01000101 00100000 01010101 01010000 00001010")
	time.sleep(0.2)
	print("01000100 01001111 01001110 00100111 01010100 00100000 01000111 01001111 00001010")
	time.sleep(0.2)
	print("01010011 01110101 01000110 01100110 01100101 01110010")
	time.sleep(0.2)
	print("""
	Current transmission into hostile area!
	LEAVE IMMEDIATELY!
	...
	Mysterious binary code: Too late!
	Seems like they sent another one...
	So weak! You will never be able to fight me!
	But i am bored, so i am going to fight YOU...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	Incoming transmission from OutsideWorld.exe ...
	Sgt. BitMonger: Wow! Jesus i thought you would have died!
	Sorry, *ahem* I mean, great work soldier! Keep going, we wont be able to contact in certain parts of the computer...
	And your next area is one of them... Good luck! DO NOT TURN BACK.""")
	input("...")
	PlayerStats[4] = PlayerStats[4] + 1
	return PlayerStats
def level1(PlayerStats):
	print("""
	You venture into a large factory looking place, many packages of binary zipping past your face.
	Getting sucked up into nodes found all around the ceiling of this place.
	There is very little light, and the temperature of the place is pretty warm.
	This feels like the CPU...""")
	input("...")
	print("""
	You remember what BitMonger told you right before the drop,
	'The Antivirus is somewhere in the Operating system.' You just have to find it.
	You venture further into the wild west of computer parts, starting to gain an understanding for what is going on.""")
	input("...")
	print("""
	You observe the binary traveling through this seemingly endless warehouse.
	All over the place, millions of 1's and 0's sporadically moving around the place.
	You see a flash of red, thinking to your self, what could it be?""")
	input("...")
	Fight.fight(PlayerStats)
	input("...")
	print("""
	Incoming transmission from: OutsideWorld.exe:
	You keep impressing me more and more, you might actually have a chance.
	Keep going, we have detected more processing of malicious programs.
	Great work soldier!
	*End Transmission*
	""")
	input("...")
	print("""
	You slip into a transmission tube, wondering where your next destination will be...""")
	input("...")
	return PlayerStats
def level2(PlayerStats):
	print("""
	The transmission tube finally ended. 
	You scramble to find another tube to finally get out of this retched place.
	While you look around, you see what seems like a large blockade of parts of metal wire and fiber,
	clogging a large hole of wire, making the fit through the next transmission tube terrifyingly small.
	As you travel to the tube, you see a strange entity, trying to squeeze it's self through the blockade.
	It looks like it it running away from something, something big...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	After murking the strange entity, you feel determined to carry on...""")
	input("...")
	print("""
	You squeeze into the transmission tube, preparing yourself for the journey ahead.
	You enter the blockade, it's reason for being there becoming more apparent, it is a resistor.
	Slows down traffic so the cpu does not get overwhelmed. With this revelation, you know that
	you are leaving  the CPU. You carry on...""")
	input("...")
	return PlayerStats
def level3(PlayerStats):
	print("""
	Incoming transmission from OutsideWorld.exe:""")
	time.sleep(2)
	print("""
	Sgt. BitMonger: Soldier, you there? We lost you on our tracker, if you can hear me, please respond!
	You attempt to respond by shouting into the air, with every time you shout you realise there is no echo.
	Testing if an echo will come from another direction you start turning around and shouting in different directions...""")
	input("...")
	print("AHHHH!")
	time.sleep(1)
	print("...")
	time.sleep(1.5)
	print("Noting. You turn around again...")
	time.sleep(2.25)
	print("AHHHH!")
	time.sleep(1.2)
	print("...")
	time.sleep(0.9)
	print("""
	Sgt. BitMonger: There we go, got you now, all systems are good, you can now proceed""")
	time.sleep(3)
	print("""
	Being a little startled from that, you cautiously proceed... Thinking to yourself, how can they find you 
	and tell you things if this is all hostile computer space? You put that though aside as you come across a strange 
	looking break in the path, In binary there is a rusty, old and broken sign that displays the words ?????
	(How something is old in binary... I have no clue)""")
	input("...")
	print("""
	You try to read the sign, many letters are missing or distorted...""")
	time.sleep(3)
	EndScreenGI.levelart1()
	input("...")
	print("""
	Do you press further, disregard the sign? Of course you do! There is no way out otherwise...""")
	input("...")
	Fight.fight(PlayerStats)
	input("...")
	print("""
	After absolutely massacring the enemy, you feel more motivated to carry on...""")
	input("...")
	return PlayerStats
def level4(PlayerStats):
	print("""
	You travel through a barron wasteland, nothing seems to be happening
	The floor is a dark green and the sky... well there is no sky!""")
	input("...")
	print("""
	Looking around, you see a faint structure in the distance...
	With every step you take, the structure becoming more apparent.
	The structure looks like a set of 2 towers, very long and high, but for some reason very thin.
	You feel the air around you becoming increasingly static, it seems the closer you get the more of it you feel.""")
	input("...")
	print("""
	Looking around the bottom of the towers you notice very little detail in the walls, wondering to yourself...""")
	print("""
	How do i get in? You keep searching further and further.""")
	input("...")
	print("""
	You come acrost a door, you notice a small slit around head height,
	you start banging on the door trying to get the attention of anyone on the other side. """)
	input("...")
	print("""
	The slit slides open and you are greeted with the glowing eyes of some monster...""")
	print("""
	Monster: Hmmph What do you want?""")
	input("...")
	print("""
	You think to yourself for a second then say, 'I want to get in'""")
	print("""
	Monster: Not without a fight...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	The door creates a shuttering noise, almost like huge bolts are moving inside...
	With a loud burst of air the door swings open and reveals a dark inside, no clue what any of this is, you proceed...""")
	input("...")
	return PlayerStats
def level5(PlayerStats):
	print("""
	Looking ahead, you can see nothing, blinded by the darkness, this worries you.
	What is there, is there even anything in here... That question left seemingly unanswered.
	Sliding your hands against the nearest wall you feel a large leaver. Pulling it, at first nothing happens,
	Then all of a sudden a loud alarm starts, in the distance a red flashing light blinks, loud electrical zapping noises ensue.""")
	input("...")
	print("""
	A booming voice sounding like it is coming from the ceiling, still unaware of what is in the room you stay still
	Mysterious voice: INTRUDER DETECTED - INTRUDER DETECTED - DELETION AUTHORISED
	The voice repeating it's self over and over.""")
	input("...")
	print("""
	You hear something shout HEY! Who are you? From behind you.
	Thinking that you can negotiate your way past this creature, you respond with, 'Oh, i just got lost, i can leave if you want?'
	Creature: Hahaha you won't get out of here alive, if that is what you were thinking...
	Feeling a zap of electricity hit you on the back of the head, it knocks you to the ground, truning around.
	You see a glowing mass come towards you, you know that this is an attack...""")
	input("...")
	Fight.fight(PlayerStats)
	input("...")
	print("""
	The lights flicker on, the room is alot smaller than you think, just big enough to fit you comfortably...
	You leave the room, as it has no further doors or way to go.
	Leaving the room, notice that you are no longer where you were before.
	This is not the outside anymore, it is just another room, completely whited out, there are no distinctions in any direction.
	You look back, where you just came from is no longer there...
	What is going on? Where am I? Where is Sgt. BitMonger?""")
	return PlayerStats
def level6(PlayerStats):
	print("""
	How did the shop guy get here? That must mean that there is someway to get out of here...""")
	print("""
	With this knowledge you feel fueled to power on...
	Walking into the white space of this room, you have no feeling of proximity, nothing is close to you but nothing if far either...
	Taking every step with caution as there is no sign of anything, no edges, colors, movement, nothing.
	Step after step, noting changes. Until, there is nothing under you, the floor disappears beneath you.""")
	input("...")
	print("""
	You hit the ground hard, pain shoots all throughout your back, unable to move you scream in pain.
	Mustering up all the strength you can, you pull yourself up, stumbling in any direction...
	The ground now has color and texture, looking around, everything now looks somewhat back to normal, well, computer normal.
	The walls are still metal and copper, and there is still the feeling of static in the air.""")
	input("...")
	print("""
	That must have been the storage of the computer, well, what was left of it...
	Venturing on you show no sing of stopping, well that is what the enemy thinks too.
	There are many bends and forks in the road, each going to vastly different areas.
	You feel lost...""")
	input("...")
	print("""
	*Ring-Ring Ring-Ring Ring-Ring* The sound of an old phone pierces your ears, the noise getting louder and louder.
	It stops and a voice proceeds...
	Sgt. BitMonger: Soldier, you still there? At last, we finally got you! We have been trying to find you forever.
	Well I must cut to the chase, you have multiple hostiles inbound, looks like a whole army! You have to divert and hide!
	It is your only h-
	The call ends abruptly, like something cut it off.""")
	input("...")
	print("""
	You limp through the paths, still in pain from the fall, trying to find a good place to hide.
	The screech of the fast traveling creatures getting louder and louder, coming from behind you...
	You turn and prepare for the worst...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	There seems to be no sign of any other creatures,
	You are a little battered up but overall in good enough shape to continue your mission.
	Walking on, in the distance you see what resembles a huge fan, nothing like what you have ever seen,
	It is spinning fast, way too fast for anything of this size...""")
	input("...")
	return PlayerStats
def level7(PlayerStats):
	print("""
	Getting closer to the fan, the air around you gradually gets hotter. The heat radiating from the fan.
	Maybe that is why it is there, to cool down the place, well it is not doing a good job at it.
	Moving closer to the centre, the heat still getting stronger, almost like a barrier, stopping anything from getting close.
	You push on, squinting your eyes as you feel them burning up, reaching the structure in a few more grueling steps.""")
	input("...")
	print("""
	This must be important, if there is such energy being used to make this heat...
	Scouring the structure for an entrance, you see a grate, walking up to this, you feel even warmer air escaping from it.
	Peering into the hole on the wall, you see what looks like a large room filled with these creatures...
	The are moving sporadically, with no direction in sight, this must be their hub!""")
	input("...")
	print("""
	Hey! A loud voice beams. You feel a hard tap on your back, slowly turning around,
	You are greeted with 3 of these creatures.
	They stare you down, with a small smirk, like they are plotting you get you.
	Noticing this, you take a run for it, running as hard as you can. The thought of imminent death fueling you...""")
	input("...")
	print("""
	You run to the end of the wires, thankfully there are no places to hide around here,
	There is nothing around here, just a straight line, you and a hole in the wire.
	Almost a godsend, this hole is just big enough to fit you, slipping through, you see the creatures fly across the top.
	Almost like it is scripted... But hey, you are still alive... right?""")
	input("...")
	print("""
	*Psst* 'I got you!' Someone says as you lay on the ground, panting from the running...""")
	Fight.fight(PlayerStats)
	print("""
	'Wow, even after all that running, You were still able to get that monster... Amazing...'
	A small green snail creature says looking at you with obnoxiously large eyes like the cute dogs and cats.
	You take this as motivation to carry on.
	You keep traveling through the tube...""")
	input("...")
	return PlayerStats
def level8(PlayerStats):
	print("""
	Damn, it is taking a long time to get the the Antivirus...
	Where is this thing anyways...
	Questions fill your head as you doubt everything you are doing...
	What is the point...
	Why am I here..
	What did i do to deserve this...""")
	input("...")
	print("""
	This tube is long and boring, just like everywhere else in this deserted place...
	Well it is deserted in a special way, there are things here, they are somewhat living, but nothing like home.
	In the real world, where you are not threatened with death and suffering on every corner that you take.
	The tube feels like it is getting bigger, more spacious, there is an end coming, you can sense it...""")
	input("...")
	print("""
	What on earth, well, on computer, is this!
	You think as you come across an inlet to another tube, but this one is different,
	It has splits in every direction imaginable, Each direction has a different name posted next to it.
	H45 | E74 | L00 | P63 | 942 | M43 | E97
	Hmm, you chose a random tube to enter, seemingly unaware to the implications of going through the wrong one.
	Death? The end? Or even worse... Even more tube?""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	Relived that it was not just more tube, you carry on.
	Coming into view of a console, this looks important, you turn around, looking at everything that is around.
	Not much, just many tubes stretching vertically across the walls,
	The cords meeting at the centre of the ceiling then going down to the console...""")
	return PlayerStats
def level9(PlayerStats):
	print("""
	Tick...""")
	time.sleep(1)
	print("""
	Tick...""")
	time.sleep(1)
	print("""
	Tick...""")
	time.sleep(1)
	print("""
	BOOM!""")
	time.sleep(2)
	print("""
	The adjacent wall explodes, launching debris towards you.
	From the initial shock of the blast you have already retreated back into the tube you came out of.
	Peering out of it like a scared animal in it's burrow, you see a single creature,
	This creature heading straight towards the console with an electronic looking device in it's carry...""")
	input("...")
	print("""
	You see a bunch of wire coiled up and connected to a tube with a switch,
	You recognise this as nothing other than an EMP!
	Realising that this will take out the whole computer, you attempt to take out the intruder...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	You now have the emp in hand, you snap some of the wires, realising that it could have been useful later...
	Shrugging this off you tap on the small screen on the console...
	But you get startled from somthing behind you...""")
	return PlayerStats
def level10(PlayerStats):
	print("""
	Looking back to the console, you start reading what it displays...""")
	input("...")
	print("""
	------  ----------  -------  -----------  -------
	|Home|  |Settings|  |Power|  |Antivirus|  |Games|
	------  ----------  -------  -----------  -------""")
	input("...")
	print("""
	FINALLY! You shout in excitement,
	All this and now you are here, ready to finish the job and destroy these creatures...
	You press the Antivirus button and press 'Run Antivirus'""")
	input("...")
	print("""
	1%""")
	time.sleep(1)
	input("...")
	print("""
	2%""")
	time.sleep(1)
	input("...")
	print("""
	3%""")
	time.sleep(1)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted""")
	time.sleep(0.25)
	print("""
	CRITICAL ERROR! Program interrupted
	What is this! You question out loud.""")
	input("...")
	print("""
	It is Me, MEMEZ.exe, the creator of all death and destruction in this universe, the unbeatable and un defeated...
	How dare you try to harm me, I am going to destroy you...
	With the power of perfect programing and deathly hacking skills,
	I have been created to destroy, and that is exactly what i intend to do...""")
	input("...")
	Fight.fight(PlayerStats)
	print("""
	MEMEZ.exe: How- How have you defeated me...
	You are hacking, you must be, i am impossible to defeat.""")
	input("...")
	print("""
	You respond,
	Hahaha well i guess not...
	Burn in hell MEMEZ...""")
	input("...")
	print("""
	The creature explodes into broken binary, scattering everywhere. The fight is over, you have won...""")
	return PlayerStats