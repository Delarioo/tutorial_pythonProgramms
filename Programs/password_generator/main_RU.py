# */--НАСТРОЙКИ---

file_open = 	True 	# Необходимо ли открывать текстовый файл, в который был записан пароль сразу послее выполнения программы
# --------------*/

from os import system							#Необходимо для запуска текстовика и очистки консоли
from random import randint as rand 				# Рандом случайного целого числа (int) в диапозоне. Параметры (начальное число(int), конечное число(int))


# -------------------------------------------------------------------------------------------
#Программа
def main():
	

	while(True):
		
		text = "Выберете шаблон:\n1 - Классический генератор паролей\n2 - Простой и Надежный шаблон "
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

#--- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
def getRandomChar(text):
	return text[rand(0,len(text)-1)]

def getResult(result):
	text = "\nВаш пароль: "+result+"\n\n**********************\n"
	printText(text)

	file = open('pass.txt', 'w')
	file.write(result)
	file.close()


	print("ПРОГРАММА ЗАВЕРШЕНА\n\n**********************\n")
	if file_open: system("notepad 'pass.txt'")
	print("Файл сохранен в 'pass.txt'")

def printText(text):
	system('cls||clear')
	print("ГЕНЕРАТОР ПАРОЛЕЙ 1.4\n")
	print("**********************\n")
	print(text)
# -------------------------------------------------------------------------------------------
#--- ШАБЛОНЫ
def pattern_classic():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	nums 	= "1234567890"
	symbols = "#$_[].=+-|"	#Для добавления спец. символов прописывайте их слитно
	chars 		= ''
	result_t 	= ''
	pass_len 	= 0
	pass_chose 	= 0
	while(True):
		text = "Длина пароля от 1 до 128 : "

		printText(text)
		try:
			pass_len = int(input())
			if pass_len >= 1 and pass_len <= 128:
				break
		except:
			continue

	while(True):
		try:
			text = "Укажите какие символы стоит использовать (1-4)\n1 - Только буквы\n2 - Только цифры\n3 - Буквы + цифры\n4 - Буквы + цифры + спец. символы"

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
		text = "Использовать спец. символы?\n1 - Да\n2 - Нет"
		printText(text)
		value = int(input())
		if value == 1:
			while (True):
				text1 = "Сколько спец. символов нужно использовать? ( 1 - 4 ) "
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
#Старт программы
main()
