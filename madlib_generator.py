

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

print(user_word_input())