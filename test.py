import sys
from random import randint


def main():
	# Taking user input for minimum and maximum faces of dice
	try:
		num = input('Enter minimum faces of Dice: ')
	except:
		print 'Input number is not string, enter valid number: '
		main()
	min_face = check_input(num)
	try:
		num = input('Enter mmaximun faces of Dice: ')
	except:
		print 'Input number is not string, enter valid number: '
		main()
	max_face = check_input(num)	
	# retieve randon number
	random_num = get_random(min_face, max_face)
	print 'your dice value is: ', random_num

# function to generate randon number
def get_random(min_dice_value, max_dice_value):
	return (randint(min_dice_value, max_dice_value))

# function to check if input number is not zero
def check_input(number):
	if number == 0:
		print 'Minimum faces should greater then zero, enter valid number'
		return main()			
	else:
		return number	 

if __name__ == '__main__':
	print '***Welcome to rolling Dice Game!***'
	main()

			
	

	





		
			