##################
# MILESTONE PROJECT 1 #
##################

# create a Tic Tac Toe game for 2 players

# 2 players playing the game at the same computer
# the board should be printed out every time a player makes a move
# accept input of the player position and then place a symbol on the board

def tictactoe_board(board):
	print('\n'*100)
	# creates 100 tabbed spaces so it "clears the screen"
	print('     |     |')
	print('  ' + (board[0][0]) + '  |  ' + (board[0][1]) + '  |  ' + (board[0][2]))
	print('     |     |')
	print('- - - - - - - - -')
	print('     |     |')
	print('  ' + (board[1][0]) + '  |  ' + (board[1][1]) + '  |  ' + (board[1][2]))
	print('     |     |')
	print('- - - - - - - - -')
	print('     |     |')
	print('  ' + (board[2][0]) + '  |  ' + (board[2][1]) + '  |  ' + (board[2][2]))
	print('     |     |')
	# sets up the board so it can be marked using indexing


def player_input():

	print('\n')
	response = input('Player1, would you like to be X or O?: ').upper()

	while not (response == 'X' or response == 'O'):
		# while answer is not X or O, it'll continue to ask
		print('Please choose between X or O: ')
		print('\n')
		response = input('Player1, would you like to be X or O?: ').upper()

	if response == 'X':
		return ('X','O')
		# tried assigning X and O to individual markers like player 1 or player
		## 2 but then it wouldn't work bc player 1 is allowed to choose


	elif response == 'O':
		return ('O','X')
		# returns a tuple which will later be assigned as markers for player 1
		## and player 2


def place_marker(board, marker, position):
	# marks the position with player 1 marker ('X') or player 2 marker ('O')
	board[position] = marker


def win_check(board, marker):
	# checks for a win by returning a boolean value of all possible win
	## combinations

	# tried making a possible winning combination equal to just one marker
	## statement but it didn't work
	# so I had to check if each individual index position is equal to marker

	return ((board[7] == marker and board[8] == marker and board[9]) 
	== marker) or ((board[4] == marker and board[5] == marker and board[6]) == 
	marker) or ((board[1] == marker and board[2] == marker and board[3]) 
	== marker) or ((board[7] == marker and board[4] == marker and board[1]) 
	== marker) or ((board[8] == marker and board[5] == marker and board[2]) 
	== marker) or ((board[9] == marker and board[6] == marker and board[3]) 
	== marker) or ((board[7] == marker and board[5] == marker and board[3]) 
	== marker) or ((board[9] == marker and board[5] == marker and board[1]) == marker)


import random

def choose_first():
	# randomly chooses a first player and returns the variable for later use
	first_player = random.randint(1,2)

	print(f'Player{first_player} will go first!')

	return first_player
	# variable assigned so that the first player can go first



def space_check(board,index1,index2):
	# returns a boolean value of whether the space is available or not
	return board[index1][index2] == ' '



def full_board_check(board):
	# if the board is full it will return True, else return False
	for i in range(1,10):
		if space_check(board,i) == True:
			return False
	return True



def player_choice(board):

	index1 = 0
	index2 = 0
	
	# space_check checks if the space is available and position not in makes sure
	## that while the board is empty it'll ask for the input

	while space_check(board,index1,index2) == False or index1 not in (1,2,3,4,5,6,7,8,9):
		
		index1 = int(input('Which row would you like place in (0,1, or 2)?: ')) 
		index2 = int(input('And which column (1,2, or 3)?: '))


	return index1
	return index2




def replay():
	replay_response = input('Would you like to play again? Yes or No: ').capitalize()

	if replay_response == 'Yes':
		return True
	else:
		return False


# ACTUAL GAME #


print('\n')
print('Welcome to Tic Tac Toe!')
want_to_play = True

while want_to_play == True:
	# starts and restarts the game

	game_board = [
		[' ',' ',' '],
		[' ',' ',' '],
		[' ',' ',' ']
	]
	# empty board

	player1,player2 = player_input()
	# assigns a marker to player1 and player2 by tuple unpacking

	print(f'Great! Player1 is {player1} and Player2 is {player2}.')

	first_player = choose_first()
	# chooses the first player randomly and assigns the variable name

	game_on = True
	# while they want to play, the while loop runs

	while game_on:

		if first_player == 1:
			print('\n')

			position = player_choice(game_board)
			# assigns the position the player wants to mark to variable name

			place_marker(game_board,player1,position)
			# marks the game board with their marker, first item in tuple

			tictactoe_board(game_board)
			# prints out the board with the marked index positions

			if win_check(game_board, player1):
				print('Congrats! Player1 has won!')

				if replay(): #== True:
					# do not have to set it to boolean?
					game_on = False
				else:
					game_on = False
					want_to_play = False

			elif full_board_check(game_board):
				print("It's a tie!")

				if replay():
					game_on = False
				else:
					game_on = False
					want_to_play = False

			else:
				first_player = 2
				# starts second player's turn

		else:
			print('\n')

			position = player_choice(game_board)

			place_marker(game_board,player2,position)

			tictactoe_board(game_board)

			if win_check(game_board, player2):
				print('Congrats! Player2 has won!')

				if replay() == True:
					game_on = False
				else:
					game_on = False
					want_to_play = False

			elif full_board_check(game_board):
				print("It's a tie!")

				if replay():
					game_on = False
				else:
					game_on = False
					want_to_play = False
			else:
				first_player = 1
else:
	print('Thanks for playing!')
	want_to_play = False
	# ends the while loop bc players do not want to play anymore



