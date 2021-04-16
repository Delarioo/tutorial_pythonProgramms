# */--SETTINGS---

file_open = 	True 	# Is it necessary to open a text file in which the password was written immediately after the program was executed
# --------------*/

from os import system							
from random import randint as rand 			


# -------------------------------------------------------------------------------------------
#Programm
def main():
	

	while(True):
		
		text = "Choose a template:\n1 - Classic password generator\n2 - Simple and Reliable Template "
		printText(text)
		try:
			value = int(input())
			if value == 1:
				getResult(pattern_classic())
				break
			elif value == 2:
				getResult(pattern1())
				break
		except:
			continue

#--- Functions
def getRandomChar(text):
	return text[rand(0,len(text)-1)]

def getResult(result):
	text = "\nYour Password: "+result+"\n\n**********************\n"
	printText(text)

	file = open('pass.txt', 'w')
	file.write(result)
	file.close()


	print("Program completed \n\n**********************\n")
	if file_open: system("notepad 'pass.txt'")
	print("Password saved in'pass.txt'")

def printText(text):
	system('cls||clear')
	print("Password generator 1.4\n")
	print("**********************\n")
	print(text)
# -------------------------------------------------------------------------------------------
#--- Patterns
def pattern_classic():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	nums 	= "1234567890"
	symbols = "#$_[].=+-|"
	chars 		= ''
	result_t 	= ''
	pass_len 	= 0
	pass_chose 	= 0
	while(True):
		text = "Password length from 1 to 128 : "

		printText(text)
		try:
			pass_len = int(input())
			if pass_len >= 1 and pass_len <= 128:
				break
		except:
			continue

	while(True):
		try:
			text = "Specify the number of character groups (1-4)\n1 - Letters\n2 - Numbers\n3 - Letters + Numbers\n4 - Letters + Numbers + Special symbols"

			printText(text)
			pass_chose = int(input())				
			if pass_chose == 1:
				chars = letters
			elif pass_chose == 2:
				chars = nums
			elif pass_chose == 3:
				chars = letters+nums
			elif pass_chose == 4:
				chars = letters+nums+symbols
			else:
				continue
			break		
		except:
			continue

	for i in range(pass_len):
		result_t += getRandomChar(chars)
	return result_t

def pattern1():
	lets_big 		= "BCDFGHJKLMNPRSTVWXZ"
	lets_small 		= "bcdfghjklmnprstvwxz"
	lets_small_vo 	= "aeiouy"
	symbols = "#$_[].=+-|"
	result = getRandomChar(lets_big)+getRandomChar(lets_small_vo)+getRandomChar(lets_small)+getRandomChar(lets_big)+getRandomChar(lets_small_vo)+getRandomChar(lets_small)+str(rand(1000,9999))
	while(True):
		text = "Use special symbols?\n1 - Yes\n2 - No"
		printText(text)
		value = int(input())
		if value == 1:
			while (True):
				text1 = "How many special symbols should be used? ( 1 - 4 ) "
				printText(text1)
				try:
					value1 = int(input())
					if value1 >= 1 and value1 <= 4:
						for i in range(value1):
							result += getRandomChar(symbols)
						break
				except:
					continue
		elif value == 2:
			break

		break

	return result
# -------------------------------------------------------------------------------------------
#Program start
main()
