

def user_word_input():

	madlib_dict = {
		'noun':' ',
		'plural noun 1':' ',
		'verb 1':' ',
		'verb 2':' ',
		'part of body':' ',
		'adjective 1':' ',
		'plural noun 2':' ',
		'adjective 2':' '
		}

	madlib_dict['noun'] = str(input('Please enter a noun: '))

	madlib_dict['plural noun 1'] = str(input('Please enter a plural noun: '))

	madlib_dict['plural noun 2'] = str(input('Please enter in another plural noun: '))

	madlib_dict['verb 1'] = str(input('Please enter a verb (present tense): '))

	madlib_dict['verb 2'] = str(input('Please enter in another verb (present tense): '))

	madlib_dict['part of body'] = str(input('Please enter in a part of the body (plural): '))

	madlib_dict['adjective 1'] = str(input('Please enter in an adjective: '))

	return madlib_dict


def madlib_template(dictionary):

	print('\n'*2)
	print('Today, every student has a computer small enough to fit into their ' + dictionary['noun'] + '.')
	print("They can solve any math problem by simply pushing the computer's little " + dictionary['plural noun 1'] + '.')
	print('Computers can add, multiply, divide, and ' + dictionary['verb 1'] + '.')
	print('They can also ' + dictionary['verb 2'] + ' better than a human.')
	print('Some computers are ' + dictionary['part of body'] + '.')
	print('Others have a/an ' + dictionary['adjective 1'] + ' screen that shows all kinds of ' + dictionary['plural noun 2'] + ' and ' + dictionary['adjective 2'] + ' figures.')
	print('\n'*2)


def replay():
	replay_response = input('Would you like to create another madlib? Yes or No: ').capitalize()

	if replay_response == 'Yes':
		return True
	else:
		return False



