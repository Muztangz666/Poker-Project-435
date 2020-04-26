# CSC 435-001
# Colin McCarthy, Brandon Miles
#
# Installations:
# Pygame: python -m pip install pygame
# PyDealer: python pip install pydealer
# 
# References:
# For setting a background image: https://self-learning-java-tutorial.blogspot.com/2015/12/pygame-setting-background-image.html
# PyDealer, for card and deck management: https://pydealer.readthedocs.io/en/latest/ <--- This one can be removed!
# For 'button' implementation: https://python-forum.io/Thread-Buttons-in-PyGame
# For making a game window: http://programarcadegames.com/index.php?chapter=example_code
# Some demo example games, for reference: https://www.pygame.org/docs/tut/chimp.py.html
# 										  https://www.pygame.org/docs/tut/tom_games6.html#makegames-6

import pygame, socket, sys, threading

player_count = 0
CardBack = pygame.image.load('CardPictures/Card_Back.jpg')
CardBack = pygame.transform.scale(CardBack, (103, 134))
message1 = "Waiting for players."
message2 = ""
message3 = ""
message4 = ""

# Declaring a few demo cards to test functions.
# This should be removed from final implementation!!!
Card1 = pygame.image.load('CardPictures/Ace_Spades.jpg')
Card2 = pygame.image.load('CardPictures/8_Diamonds.jpg')
Card3 = pygame.image.load('CardPictures/10_Spades.jpg')
Card4 = pygame.image.load('CardPictures/2_Hearts.jpg')
Card5 = pygame.image.load('CardPictures/Queen_Diamonds.jpg')
Card6 = pygame.image.load('CardPictures/8_Spades.jpg')
Card7 = pygame.image.load('CardPictures/5_Hearts.jpg')
Card1 = pygame.transform.scale(Card1, (169, 209))
Card2 = pygame.transform.scale(Card2, (169, 209))
Card3 = pygame.transform.scale(Card3, (103, 134))
Card4 = pygame.transform.scale(Card4, (103, 134))
Card5 = pygame.transform.scale(Card5, (103, 134))
Card6 = pygame.transform.scale(Card6, (103, 134))
Card7 = pygame.transform.scale(Card7, (103, 134))

# Updates the display each time a player joins.
def Add_Player():
	if player_count < 4:
		player_count += 1
		if player_count == 2:
			pygame.draw.rect(background, (153, 51, 0), [40, 115, 109, 140], 5)
			pygame.draw.rect(background, (153, 51, 0), [160, 115, 109, 140], 5)
			background.blit(CardBack, (43, 118))
			background.blit(CardBack, (163, 118))
		elif player_count == 3:
			pygame.draw.rect(background, (153, 51, 0), [520, 92, 109, 140], 5)
			pygame.draw.rect(background, (153, 51, 0), [640, 92, 109, 140], 5)
			background.blit(CardBack, (523, 95))
			background.blit(CardBack, (643, 95))
		elif player_count == 4:
			pygame.draw.rect(background, (153, 51, 0), [1000, 115, 109, 140], 5)
			pygame.draw.rect(background, (153, 51, 0), [1120, 115, 109, 140], 5)
			background.blit(CardBack, (1003, 118))
			background.blit(CardBack, (1123, 118))
		
def Remove_Player():
	print()

def Display_Hand():
	background.blit(Card1, (113, 428))
	background.blit(Card2, (303, 428))

def Display_Flop():
	background.blit(Card3, (346, 278))
	background.blit(Card4, (466, 278))
	background.blit(Card5, (586, 278))

def Display_Turn():
	background.blit(Card6, (706, 278))
	
def Display_River():
	background.blit(Card7, (826, 278))
	
def Update_Text(new_message, message1, message2, message3, message4):

	# Updates the messages before they are displayed.
	message4 = message3
	message3 = message4
	message2 = message3
	message1 = new_message
	
	# Displays the updated messages in the bottom right textbox.
	pygame.draw.rect(background, (153, 51, 0), [839, 425, 425, 215], 5)
	# pygame.font.SysFont sets the font to be used for text.
	textbox_font = pygame.font.SysFont('Calibri', 50, True, False)
	textbox = textbox_font.render(message4, True, (51, 204, 51))
	background.blit(textbox, (850, 435))
	textbox = textbox_font.render(message3, True, (102, 255, 102))
	background.blit(textbox, (850, 485))
	textbox = textbox_font.render(message2, True, (204, 255, 153))
	background.blit(textbox, (850, 535))
	textbox = textbox_font.render(message1, True, (255, 255, 255))
	background.blit(textbox, (850, 585))

def New_Game(image, background, text, CardBack):
	# Clears main menu buttons and text.
	background.blit(image, (0, 0))
	
	# Displays raise and fold 'buttons' in 'read-only' mode. 
	button_font = pygame.font.SysFont('Calibri', 40, True, False)
	raise_button = button_font.render("Raise", True, (178, 178, 178))
	background.blit(raise_button, (7, 400))
	fold_button = button_font.render("Fold", True, (178, 178, 178))
	background.blit(fold_button, (15, 480))
	call_button = button_font.render("Call", True, (178, 178, 178))
	background.blit(call_button, (19, 560))
	
	# Draws rectangles for hand cards.
	pygame.draw.rect(background, (153, 51, 0), [110, 425, 175, 215], 5)
	pygame.draw.rect(background, (153, 51, 0), [300, 425, 175, 215], 5)
	
	# Draws rectangles for table cards.
	pygame.draw.rect(background, (153, 51, 0), [343, 275, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [463, 275, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [583, 275, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [703, 275, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [823, 275, 109, 140], 5)
	
	# Draws rectangles for opponent cards.
	pygame.draw.rect(background, (153, 51, 0), [40, 115, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [160, 115, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [520, 92, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [640, 92, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [1000, 115, 109, 140], 5)
	pygame.draw.rect(background, (153, 51, 0), [1120, 115, 109, 140], 5)
	
	# Changes the size of the picture.
	CardBack = pygame.transform.scale(CardBack, (103, 134))
	
	# Displays card backs for opponents hands.
	background.blit(CardBack, (43, 118))
	background.blit(CardBack, (163, 118))
	background.blit(CardBack, (523, 95))
	background.blit(CardBack, (643, 95))
	background.blit(CardBack, (1003, 118))
	background.blit(CardBack, (1123, 118))
	
	# Displays game status textbox.
	pygame.draw.rect(background, (153, 51, 0), [839, 425, 425, 215], 5)
	textbox_font = pygame.font.SysFont('Calibri', 50, True, False)
	textbox = textbox_font.render(text, True, (255, 255, 255))
	background.blit(textbox, (850, 585))
	
	# Displays pot, money, and username textboxes.
	textbox_font2 = pygame.font.SysFont('Calibri', 40, True, False)
	name_textbox1 = textbox_font2.render("Player1", True, (153, 51, 0))
	name_textbox2 = textbox_font2.render("Player2", True, (153, 51, 0))
	name_textbox3 = textbox_font2.render("Player3", True, (153, 51, 0))
	name_textbox4 = textbox_font2.render("Player4", True, (153, 51, 0))
	background.blit(name_textbox1, (490, 440))
	background.blit(name_textbox2, (43, 70))
	background.blit(name_textbox3, (523, 47))
	background.blit(name_textbox4, (1003, 70))
	bet_textbox = textbox_font2.render("Current Bet: $0", True, (153, 51, 0))
	background.blit(bet_textbox, (490, 490))
	pot_textbox = textbox_font2.render("Current Pot: $0", True, (153, 51, 0))
	background.blit(pot_textbox, (490, 540))
	money_textbox = textbox_font2.render("Your Money: $1000", True, (153, 51, 0))
	background.blit(money_textbox, (490, 590))
	
	background.blit(CardBack, (346, 278))
	background.blit(CardBack, (466, 278))
	background.blit(CardBack, (586, 278))
	background.blit(CardBack, (706, 278))
	background.blit(CardBack, (826, 278))
	CardBack = pygame.transform.scale(CardBack, (169, 209))
	background.blit(CardBack, (113, 428))
	background.blit(CardBack, (303, 428))

# Client and server do not work.
def Client():
	# New socket declared.
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the same port as the server.
	#address = ('localhost', 10000)
	address = ('127.0.0.1', 10000)
	print('Client: connecting to %s port %s' % address)
	client_socket.connect(address)
	New_Game(image, background, "Waiting for host.")

def Server():
	# New socket declared.
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Bind is used to connect to local host.
	#address = ('localhost', 10000)
	address = ('127.0.0.1', 10000)
	print('Starting up on %s port %s' % address)
	server_socket.bind(address)
	
	# Listen for client.
	#server_socket.listen(4)
	
	while True:
		connection, client_address = server_socket.accept()
		print('Server: Connection successful.')

		# Manage events.
		for event in pygame.event.get():
	
			# Quits the game if object type is QUIT.
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()
				if mouse[0] > 400 and mouse[0] < (400 + button1.get_width()) and mouse[1] > 300 and mouse[1] < (300 + button1.get_height()):
					print()

		clock.tick(10)

def My_Turn():
	print()

# On startup, show background + textboxes for title and button options.
pygame.init()

clock = pygame.time.Clock()

# Declares surface object, sets the window size.
background = pygame.display.set_mode((1275, 650))
pygame.display.set_caption('Poker: Texas Hold\'em v0.0')
image = pygame.image.load(r'Capture.PNG')
image = pygame.transform.scale(image, (1275, 650))

# Display the image on the background.
background.blit(image, (0, 0))

# Displays the title.
font = pygame.font.SysFont('Calibri', 60, True, False)
title = font.render("Poker: Texas Hold'em", True, (0, 0, 0))
background.blit(title, (360, 170))

# Displays the 'buttons'.
button1 = font.render("Start a New Game", True, (250, 250, 250))
background.blit(button1, (400, 300))
button2 = font.render("Join an Existing Game", True, (250, 250, 250))
background.blit(button2, (360, 425))

# While loop manages main menu interactions.
client_flag = False
server_flag = False

# Would stay in this loop while on the main menu, exit once the client and server are running.
while True:

	# Manage events.
	for event in pygame.event.get():
	
		# Quits the game if object type is QUIT.
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if mouse[0] > 400 and mouse[0] < (400 + button1.get_width()) and mouse[1] > 300 and mouse[1] < (300 + button1.get_height()):
				print("button1")
				#server_flag = True
				New_Game(image, background, "Waiting for players.", CardBack)
				break
			elif mouse[0] > 360 and mouse[0] < (360 + button1.get_width()) and mouse[1] > 425 and mouse[1] < (425 + button1.get_height()):
				print("button2")
				#client_flag = True
				#break
		
		# Updates display for any changes made.
		pygame.display.update()
	
	if client_flag or server_flag == True:
		break
	
	# Limits loop iterations/second.
	clock.tick(10)

if server_flag == True:
	server_thread = threading.Thread(target = Server)
	server_thread.start()

client_thread = threading.Thread(target = Client)
client_thread.start()
