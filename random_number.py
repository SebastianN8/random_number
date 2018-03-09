#
# random_number.py
#
# Created by: Sebastian N
# Created on: March 8 
#
# This program compares a random number with one chosen by the user
import random

def compare_numbers(number_passed_in):
	random_number = random.randint(1, 6+1)

	if random_number == choosen_number:
		print('You got it!')
	else:
		print('No, incorrect, the number is: ', random_number)
	

choosen_number = input("Choose a number between 1 and 6: ")
result = compare_numbers(choosen_number)

input()