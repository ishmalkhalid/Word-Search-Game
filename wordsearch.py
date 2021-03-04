#----------------------------------------#
#-------------ISHMAL KHALID--------------#
#-----------------ik1299-----------------#
#----INTRODUCTION TO COMPUTER SCIENCE----#
#------------Word Search Game------------#
#----------------------------------------#

import os
import random

#print board
def printboard():

	#clear screen
	os.system('clear')

	print("+"+"---+"*CDIM)

	for row in range(RDIM):
		print("|", end='')

		for col in range(CDIM):
			print(" " + board[row][col] + " " + "|", end='')

		print("\n+" + '---+'*CDIM)
	
#check for word in 8 orientations
def findWord():

	row = 0
	rvalue = True
	cvalue = True

	while rvalue == True and row < RDIM:
		col = 0
		while cvalue == True and col < CDIM:
			#find first letter of word in board
			if board[row][col].lower() == word[0]:

				#check characters horizontally to the right
				COL = col
				ctr = 0
				for char in word:
					if COL < CDIM and board[row][COL].lower() == char:
						COL = COL + 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							COL = col
							#change to uppercase
							while COL < len(word) + col:
								board[row][COL] = board[row][COL].upper()
								COL = COL + 1
							rvalue = False
							cvalue = False
							printboard()

					else:
						break

				#check characters horizontally to the left
				COL = col
				ctr = 0
				for char in word:
					if COL > -1 and board[row][COL].lower() == char: 
						COL = COL - 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							COL = col
							#change to uppercase
							while COL > col - len(word):
								board[row][COL] = board[row][COL].upper()
								COL = COL - 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

                #check characters vertically downwards
				ROW = row
				ctr = 0
				for char in word:
					if ROW < RDIM and board[ROW][col].lower() == char:
						ROW = ROW + 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							#change to uppercase
							while ROW < len(word) + row:
								board[ROW][col] = board[ROW][col].upper()
								ROW = ROW + 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

				#check characters vertically upwards
				ROW = row
				ctr = 0
				for char in word:
					if ROW > -1 and board[ROW][col].lower() == char: 
						ROW = ROW - 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							#change to uppercase
							while ROW > row - len(word):
								board[ROW][col] = board[ROW][col].upper()
								ROW = ROW - 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

				#check characters diagonally right down
				ROW = row
				COL = col
				ctr = 0
				for char in word:
					if ROW < RDIM and COL < CDIM and board[ROW][COL].lower() == char:
						ROW = ROW + 1
						COL = COL + 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							COL = col
							#change to uppercase
							while ROW < len(word) + row and COL < len(word) + col:
								board[ROW][COL] = board[ROW][COL].upper()
								ROW = ROW + 1
								COL = COL + 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

				#check characters diagonally right up
				ROW = row
				COL = col
				ctr = 0
				for char in word:
					if ROW > -1 and COL < CDIM and board[ROW][COL].lower() == char: 
						ROW = ROW - 1
						COL = COL + 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							COL = col
							#change to uppercase
							while ROW > row - len(word) and COL < len(word) + col:
								board[ROW][COL] = board[ROW][COL].upper()
								ROW = ROW - 1
								COL = COL + 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

				#check characters diagonally left up
				ROW = row
				COL = col
				ctr = 0
				for char in word:
					if ROW > -1 and COL > -1 and board[ROW][COL].lower() == char: 
						ROW = ROW - 1
						COL = COL - 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							COL = col
							#change to uppercase
							while ROW > row - len(word) and COL > col - len(word):
								board[ROW][COL] = board[ROW][COL].upper()
								ROW = ROW - 1
								COL = COL - 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break
			
				#check characters diagonally left down
				ROW = row
				COL = col
				ctr = 0
				for char in word:
					if ROW < RDIM and COL > -1 and board[ROW][COL].lower() == char: 
						ROW = ROW + 1
						COL = COL - 1
						ctr = ctr + 1
						#check if entire word present
						if ctr == len(word):
							ROW = row
							COL = col
							#change to uppercase
							while ROW < len(word) + row and COL > col - len(word):
								board[ROW][COL] = board[ROW][COL].upper()
								ROW = ROW + 1
								COL = COL - 1
							rvalue = False
							cvalue = False
							printboard()
						
					else:
						break

			col = col + 1
		row = row + 1

#select random board
NUM_OF_BOARDS = 12
board_number = random.randint(1, NUM_OF_BOARDS)
filename = "board_" + str(board_number) + ".csv"

#open file 
try:
	inFile = open(filename, 'r')

except IOError:
	print("Sorry. File not found.")

#get dimensions
line1 = inFile.readline().strip().split(',')

RDIM = int(line1[0])
CDIM = int(line1[1])

#create a list of existing words in board
words = line1[2:]

#fill the board
board = []
for row in range(RDIM):
	line = inFile.readline().strip().split(",")
	board.append(line)

#close file
inFile.close()

#print board
printboard()

#ask for the number of players and validate input
NumOfPlayers = input("Please enter the number of players: ")
while NumOfPlayers.isdigit() == False or int(NumOfPlayers) < 2:
	NumOfPlayers = input("Please enter the number of players: ")

#choose random player
NumOfPlayers = int(NumOfPlayers)	
turn = random.randint(0, NumOfPlayers-1)

#declare list and dictionaries
WordsEntered = []
scores = {}
wordsguessed = {}

#loop until not all words are found
while len(words) != 0:

	#first player enters word
	word = input("Player " + str(turn) + ", please enter a word: ")

	#if incorrect guess (word entered before) or (not lowercase) or (less than 3 letters) or (word not in board)
	if word in WordsEntered or word.islower() == False or len(word) < 3 or word not in words:
		print("Invalid input.")

	#if correct guess
	else:
		WordsEntered.append(word)
		words.remove(word)
		findWord()
		print("Score: ")

		#increment player's score
		scores['Player ' + str(turn)] = scores.get('Player ' + str(turn), 0) + 1

		#create a list of the guessed words for each player
		wordsguessed.setdefault('Player ' + str(turn), [])
		wordsguessed['Player ' + str(turn)].append(word)

		#print all players' scores
		for key in scores:
			print(key + ": " + str(scores[key]), end=' ')
			print(wordsguessed[key])

	#alternating turns
	if len(words) != 0:
		turn = (turn + 1) % NumOfPlayers

#finding the highest score among all players
highest_score = 0
for key in scores:
	if  scores[key] > highest_score:
		highest_score = scores[key]

#concluding the winner with the highest score
for key in scores:
	if scores[key] == highest_score:
		print(key, " wins the game!")
	

#---------------------------------------#
#------------END OF PROGRAM-------------#
#---------------------------------------#