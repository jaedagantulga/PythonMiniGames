



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



def player_choice(board):

	index1 = -1
	index2 = -1
	
	# space_check checks if the space is available and position not in makes sure
	## that while the board is empty it'll ask for the input

	while space_check(board,index1,index2) == False or index1 not in (0,1,2) or index2 not in (0,1,2):
		
		index1 = int(input('Which row would you like place in (0,1, or 2)?: ')) 
		index2 = int(input('And which column (0,1, or 2)?: '))


	return (index1,index2)
	#tried returning a list and tried return individually like
	# return index 1
	# return index 2




def place_marker(board,marker,index1,index2):
	# marks the position with player 1 marker ('X') or player 2 marker ('O')
	board[index1][index2] = marker



def check_for_row_or_column_winner(board,is_row=False):

	for i in range(len(game_board)):
		
		previous_marker = None

		for j in range(len(game_board[i])):

			if is_row:
				current_marker = game_board[i][j]

			else:
				current_marker = game_board[j][i]


			if not previous_marker:
				previous_marker = current_marker
				continue

			else:

				if previous_marker == current_marker:
					# is_final_marker = j == len(game_board[i])-1
					if j != len(game_board[i])-1:
						continue

					# if not is_final_marker:
					#  	continue

					else:
						return True
				
				else:
					break
	return False




def check_for_diagonal_winner(board,left_diagonal=False):
# ,left_diagonal=False):

	previous_marker = None

	for i in range(len(game_board)):
		

		if left_diagonal:
			current_marker = game_board[i][i]

		else:
			# b = len(board)
			current_marker = game_board[i][len(board)-1-i]


		if not previous_marker:
			previous_marker = current_marker
			continue

		else:
			if previous_marker == current_marker:
				if i != len(game_board[i])-1:
						continue

					# if not is_final_marker:
					#  	continue

				else:
					return True

			else:
				return False




def check_for_winner(board):

	check_for_row_or_column_winner(game_board,True)

	check_for_row_or_column_winner(game_board)

	check_for_diagonal_winner(game_board,True)

	check_for_diagonal_winner(game_board)



def full_board_check(board):
	# if the board is full it will return True, else return False
	for i in range(len(board)):
		#if space_check(board,index1,index2) == True:
		for j in board[i]:
			
			if j == ' ':
				return False
	return True



def replay():
	replay_response = input('Would you like to play again? Yes or No: ').capitalize()

	if replay_response == 'Yes':
		return True
	else:
		return False




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

			#position = 
			index1,index2 = player_choice(game_board)
			# assigns the position the player wants to mark to variable name

			place_marker(game_board,player1,index1,index2)
			# marks the game board with their marker, first item in tuple

			tictactoe_board(game_board)
			# prints out the board with the marked index positions

			if check_for_winner(game_board):
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

			#position = 
			index1,index2 = player_choice(game_board)

			place_marker(game_board,player2,index1,index2)

			tictactoe_board(game_board)

			if check_for_winner(game_board):
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
