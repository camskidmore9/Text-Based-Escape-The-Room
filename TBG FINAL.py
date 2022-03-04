print('Cameron Skidmore - 7th Period')

'''vvvThis is the begining of the game. It will welcome the player and ask for their name'''
print('Welcome to this escape the room text based game. In order to win this game you \nwill need to find to escape.')
name = input('What is your name? ')
name = name.title().rstrip()
'''^^^END OF BEGINNING'''


#This is some more basic introduction for the player
print('\nHello, ' + name + ". You are trapped in a room. The object of this game is for you to escape the room. In order to do this you must move around and search for the items and clues to get the key and unlock the door. Before we begin, let's set up some controls.")

'''vvvvThis section has the user define what they want to type in order to move in a certain direction and define a function to print their commands'''
l_dir = input('\nWhat would you like to type to move left? ')
r_dir = input('\nWhat would you like to type to move right? ')
f_dir = input('\nWhat would you like to type to move forward? ')
b_dir = input('\nWhat would you like to type to move back? ')

#This dictionary takes the values the user inputted for the directions and sorts them
directions = {
	'left': {
		'direction': 'Left',
		'command': l_dir,
		},
	'right': {
		'direction': 'Right',
		'command': r_dir,
		},
	'forward': {
		'direction': 'Forward',
		'command': f_dir,
		},
	'back': {
		'direction': 'Back',
		'command': b_dir,
		},
	}
		

#This function takes all of the chosen directions from the dictionary and prints them in an easy-to-read manner
def direct():
		print('Your assigned directions are:')
		for direction, info in directions.items():
			print('\nDirection: ' + direction)
			print('Command: ' + info['command'] + '\n ')


direct()
'''^^^END OF DIRECTION COMMAND SETUP'''

'''vvvvThis next section will define all of the variables and items the program needs in order to function'''

#This list will store all of the items the player collects. As they find items, they will be added to the list. When they use them, they will be removed.
items = []

#Hints variable. The player starts with 3 variables. They can use them at certain points of the game. They will be prompted when they can use them.
global hints
hint = 3

#This is the power variable. It indicates whether the vending machine is on. When the power is turned on, it will be set to 1
global power
power = 0

'''^^^END OF VARIABLES'''

#Some more instruction for the user before the game begins.
print("We are almost ready to start. \nThroughout the game you will be asked to use these direction commands. \nIf you forget your commands, simply type 'commands' and it will print them off. \nAlso, you start with 3 hints. Whenever you are asked to choose a direction, you can type 'hint' and it will give you a hint for that area.\nUse them carefully, \nonce you run out, they're gone. Let us begin \n  \n ")

'''vvvvThe next section will define some essential functions that are needed at certain points throughout the game'''


#Keypad function: This function will be called within the vending machine area function. It is how the player will operate the keypad of the vending machine
def keypad():
	ans = input('What code would you like to put in?')
	ans = ans.lower()
	#Asks the user to input a value for an item, like a real vending machine
	if ans == 'c7':
	#Checks to see if they have money. If not, doesn't dispense
		if 'money' in items:
			ans = input('Would you like to deposit your money(yes/no)')
			ans = ans.lower()
			if ans == 'y' or ans == 'yes':
				items.remove('money')
				print('You insert the money and the key begins to move. It falls into the tray and you grab it.')
				items.append('key')
				machdir()
			else:
				print('OK. Maybe later.')
				machine()
		else:
			print('You do not have the required funds. Sorry')
			machine()
	else:
		print('That item is not cuurently available. Try again later.')
		machine()

#Whenever the user asks for directions to be printed. This variable will do that
def direct():
		print('Your assigned directions are:')
		for direction, info in directions.items():
			print('\nDirection: ' + direction)
			print('Command: ' + info['command'] + '\n ')
			

#Plant search: This will be called during the plant area function. It is a while loop that has them search throuh until they find something or give up
def plantsearch():
	while True:
		ans = input('Where on the ficus would you like to look? (Enter "quit" at any poin to stop searching)')
		ans = ans.lower().rstrip()
		if ans == 'behind' or ans == 'rear' or ans == 'in the back':
			print('You look behind the plant and see "C7" written on the wall.')
			break
		elif  ans == 'quit':
			plantdir()
		elif ans == 'inside' or ans == 'in':
			items.append('money')
			print('You have found money! Spend it wisely')
			plant()
		else:
			print('There is nothing to see in this part of the ficus.')
			

'''^^^^END OF ESSENTIAL FUNCTIONS'''			
			
			
'''vvvvThis neext section will define the area functions. They will run when a user enters an area'''


#Locker: When the player enter the locker area, they will enter this function. They must have the combination and they will acquire the power cable for the vending machine
def locker():
	ans = input('\nThere is a locker in front of you. Would you like to open it. (y or n)')
	#Asks them if they want to try and open the locker
	if ans == 'y':
		ans = input('\nThere is a combination lock on the locker. Do you know the combination? (y or n)')
		ans = ans.lower()
		#Asks if they know the combination
		if ans == 'y' or ans == 'yes':
			combo = input('What is the combination?')
			combo = combo.lower()
			combo = combo.rstrip()
			#tests to see if they got the combination correct
			if combo == '82739' or combo == 82739:
				print('')
				#If they get the combination lock, it will check to see if they have the cable then decide whether to give it to them or not
				if 'cable' in items:
					print('The locker opened. There is nothing inside because you already have the cable.')
					locker()
				else:
					items.append('cable')
					print('\nThe lock opened and you open the locker. Inside you find a power cable.')					
					locker()
			else:
				ans = input('Sorry. That is not the right combination.')
				locker()
		else:
			print('OK. Come again')
			locker()
	elif ans == 'n':
		lockdir()
	else:
		print('That is not a valid command')
		locker()

	
#Front door: The 'final' code for they game. Will check to see if they have the key. If they do, they will win and escape. If not, they must continue
def frontdoor():
	if 'key' in items:
		print('Congratulations ' + name + '. You win!')
		import ending.py
		ending.py
		
	else:
		print('Sorry. The door is locked. Keep trying to find the key')
		doordir()

	
#Vending machine: This is the vending machine area. They must put the power cable in the back then type in the right ID for they key to be dispensed
def machine():
	global power
	ans = input('You are standing in front of the vending machine. There is a display window and a keypad. \nYou can look at anywhere on the machine, where would you like to look?(type "quit" at any time to stop)')
	ans = ans.lower().rstrip()
	#Asks which part of the machine they would like to look at
	if ans == 'window' or ans == 'display' or ans == 'displaywindow':
		print('Inside the machine, there is only 1 item. It is a key. The number to type has been removed.')
		machine()
		#If they look at the keypad, they will be prompted to type in a number. If they have turned on the power, they will be able to input commands until they get the right one. If not, they must turn the power on first.
	elif ans == 'keypad' or ans == 'pad' or ans == 'key':
		if power == 1:
			ans = input('You move to inspect the keypad. It has various numbers and letters.\nWould you like to put in a number? (yes/no)')
			ans = ans.lower()
			if ans == 'y' or ans == 'yes':
				keypad()
			elif ans == 'n' or ans == 'no':
				print('Maybe later.')
				machine()
			else:
				print('Sorry. That is not a valid command.')
				machine()
		else:
			print('You move to inspect the keypad. The machine appears to be off. Try again when it is on.')
			machine()
	elif ans == 'quit':
			machdir()
	elif ans == 'behind' or ans == 'back' or ans == 'theback':
		if power == 1:
			ans = input('You have already turned on the power. Press "Enter" to continue')
			machine()
		else:
			print('You peer behind the machine.\nThere appears to be a slot and a plug to insert the cable')
			if 'cable' in items:
				ans = input('Would you like to insert the power cable?(yes/no)')
				ans = ans.lower()
				if ans == 'yes' or ans == 'y':
					power = 1
					print('You plus the cable into the machine and it whirrs to life')
					machine()
				else:
					print('You either answered no or an incorrect command. Please come again.')
					machine()
			else:
				print('There appears to be a slot for a power cable')
				machine()
	else:
		print('Sorry. That is not a valid command.')
		machine()
			
#Plant: Here they will be able to do 2 things. Find the money and they code for the key in the vending machine.
def plant():
	print('You approach the plant. It appears to be a ficus.')
	ans = input('Would you like to take a closer look?(yes/no)')
	ans = ans.lower()
	#If they choose to search the ficus, they will be able to type locations to check until they find it or give up
	if ans == 'yes' or ans == 'y':
		plantsearch()
	else:
		print('Ok. Thank you for coming to look at this ficus. Come again soon!')
		plantdir()		

#Fish tank: This section is a red herring. They can search and search it and won't find anything
def tank():
	print('There appears to be something in the tank.')
	ans = input('Would you like to search it?(yes/no)')
	ans = ans.lower()
	if ans == 'yes' or ans == 'y':
		print('You reach your hand into the fish tank. Nothing in here except fish poop.')
		tankdir()
	else:
		print('Ok. Maybe later. Come again.')
		tankdir()
		
		
#Frame: The picture frame is where they will be able to find the combination to the locker. It is located on the back of the frame
def frame():
	print('You move forward towards the picture frame. You can now search it')
	#They can type in locations to their hearts content. They must think to check the back to find the combination
	while True:
		ans = input('Where on the frame would you like to look? (Enter "quit" at any poin to stop searching)')
		ans = ans.lower().rstrip()
		if ans == 'behind' or ans == 'rear' or ans == 'in the back' or 'behind':
			print('You flip the painting over and see the number 82739 writte on the back.')
			framedir()
		elif  ans == 'quit':
			framedir()
		elif ans == 'picture' or ans == 'painting' or ans == 'front':
			print('It is a lovely picture of a dog.')
		else:
			print('There is nothing to see in this part of the frame.')
	
			
'''^^^^END OF AREA FUNCTIONS'''

'''vvv The next section is the direction commands. The user will encounter direction commands in order to move around the room. These are where they can ask for commands or use hints'''

#Plant direction
def plantdir():
	ans = input('You are standing in front of a potted plant. Which direction would you like to move.')
	ans = ans.lower()
	if ans == l_dir:
		print('You move around the corner to the door')
		doordir()
	elif ans == f_dir:
		plant()
	elif ans == b_dir:
		middle()
	elif ans == r_dir:
		machdir()
	elif ans == 'commands':
		direct()
	elif ans == 'hint':
		global hint
		hint = hint-1
		print('You could check inside or behind the ficus.')
		plantdir()
	else:
		print('Sorry that is not a valid command')
		plantdir()
		

#Locker direciton		
def lockdir():
	ans = input('You are standing in front of a locker. Which direction would you like to move?')
	ans = ans.lower() 
	if ans == l_dir:
		print('You move around the corner to the picture frame.')
		framedir()
	elif ans == f_dir:
		locker()
	elif ans == b_dir:
		middle()
	elif ans == r_dir:
		print('You move around the corner to the fish tank.')
		tankdir()
	elif ans == 'commands':
		direct()
	elif ans == 'hint':
		global hint
		hint = hint-1
		print('The picture frame looks pretty cool.')
		lockdir()
	else:
		print('Sorry that is not a valid command')
		lockdir()
	

#Door direction
def doordir():
	ans = input('You are in front of the door. Which direction would you like to move?')
	ans = ans.lower()
	if ans == l_dir:
		print('You move to stand in front of the fish tank')
		tankdir()
	elif ans == f_dir:
		frontdoor()
	elif ans == b_dir:
		middle()
	elif ans == r_dir:
		print('You move to stand in front of the plant')
		plantdir()
	elif ans == 'commands':
		direct()
	else:
		print('Sorry that is not a valid command')
		doordir()
	

#Vending machine direction	
def machdir():
	ans = input('You are standing in front of a vending machine. Which direction would you like to move?')
	ans = ans.lower()
	if ans == l_dir:
		plantdir()
	elif ans == f_dir:
		machine()
	elif ans == b_dir:
		middle()
	elif ans == r_dir:
		print('You move around the corner to the picture frame.')
		framdir()
	elif ans == 'commands':
		direct()
	elif ans == 'hint':
		global hint
		hint = hint-1
		print('You should take a look behind the machine.')
		machdir()
	else:
		print('Sorry that is not a valid command')
		machdir()
	
	
#Picture frame direction
def framedir():
	print('You are standing in front of a picture frame.')
	ans = input('Which direction would you like to move?')
	ans = ans.lower()
	if ans == l_dir:
		print('You move around the corner to the vending machine.')
		machdir()
	elif ans == f_dir:
		frame()
	elif ans == b_dir:
		middle()
	elif ans == r_dir:
		print('You move around the corner to the locker.')
		lockdir()
	elif ans == 'commands':
		direct()
	elif ans == 'hint':
		global hint
		hint = hint-1
		print('I think behind the picture would look pretty good.')
		framedir()
	else:
		print('Sorry that is not a valid command')
		framedir()


#Main direction. Middle of the room
def middle():
	print('You are standing in the center of the room facing the door.')
	ans = input('Which direction would you like to move?')
	ans = ans.lower()
	if ans == l_dir:
		lockdir()
	elif ans == f_dir:
		doordir()
	elif ans == b_dir:
		framedir()
	elif ans == r_dir:
		machdir()
	elif ans == 'commands':
		direct()
	else:
		print('Sorry that is not a valid command')
		middle()
	

#Fish tank direction	
def tankdir():
	print('You are standing in front of a fish tank.')
	ans = input('Which direction would you like to move?')
	ans = ans.lower()
	if ans == l_dir:
		lockdir()
	elif ans == f_dir:
		tank()
	elif ans == b_dir:
		framedir()
	elif ans == r_dir:
		doordir()
	elif ans == 'commands':
		direct()
	elif ans == 'hint':
		global hint
		hint = hint-1
		print('You just wasted a hint. The tank is a distraction. Beaned')
		tankdir()
	else:
		print('Sorry that is not a valid command')
		tankdir()
	
	
'''^^^^END OF DIRECTION FUNCTIONS'''




#This next command begins the game. It will cause the functions to loop through each other until they solve it. They will begin in the center of the room
middle()
		

input()

