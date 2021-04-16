# */--НАСТРОЙКИ---

file_open = 	True 	# Необходимо ли открывать текстовый файл, в который был записан пароль сразу послее выполнения программы
file_remove = 	False 	# Необходимо ли удалять файл с паролем сразу после закрытия окна
sys_version = "1.3.7"

# --------------*/

from os import system							#Необходимо для запуска текстовика
from os import remove							#Необходимо для удаление текстовика после открытия
from random import randint as rand 				# Рандом случайного целого числа (int) в диапозоне. Параметры (начальное число(int), конечное число(int))

#Группы символов

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nums 	= "1234567890"
symbols = "#$_[].=+-|"	#Для добавления спец. символов прописывайте их слитно

#Глобальные переменные

print("ГЕНЕРАТОР ПАРОЛЕЙ ",sys_version,"\n")
print("**********************\n\n")


# -------------------------------------------------------------------------------------------
#Программа
def main():
	chars 		= ''
	result_t 	= ''
	pass_len 	= 0
	pass_chose 	= 0

	while(True):
		
		text = "Выберете шаблон:\n1 - Классический генератор паролей\n2 - Простой и Надежный шаблон "
		print(text)
		try:
			value = int(input())
			if value == 1:
				getResult(pattern_classic())
				break
			elif value == 2:
				getResult(pattern1())
				break

			else:
				system('cls||clear')
		except:
			system('cls||clear')


#--- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
def getRandomChar(text):
	return text[rand(0,len(text)-1)]

def getResult(result):
	system('cls||clear')
	print("**********************\n\nВаш пароль: ",result,"\n\n**********************\n")

	file = open('pass.txt', 'w')
	file.write(result)
	file.close()


	print("ПРОГРАММА ЗАВЕРШЕНА\n\n**********************\n")
	if file_open: system("notepad 'pass.txt'")
	if file_remove: 
		remove('pass.txt') 
	else: 
		print("Пароль сохранен в файл 'pass.txt'")
# -------------------------------------------------------------------------------------------
#--- ШАБЛОНЫ
def pattern_classic():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	nums 	= "1234567890"
	symbols = "#$_[].=+-|"	#Для добавления спец. символов прописывайте их слитно
	while(True):
		text = "Длина пароля от 1 до 128 : "
		print(text)
		try:
			pass_len = int(input())
			if pass_len >= 129 or pass_len <= 0:
				system('cls||clear')
			else:
				break
			
		except:
			system('cls||clear')

	while(True):
		system('cls||clear')
		try:
			print("\n**********************\nУкажите номер групп символов (1-4)\n1 - Только буквы\n2 - Только цифры\n3 - Буквы + цифры\n4 - Буквы + цифры + спец. символы")
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
				print("\n**********************\n\nУКАЗАН НЕВЕРНЫЙ ВАРИАНТ\n")
				continue;
			break		
		except:
			print("\n**********************\n\nУКАЗАН НЕВЕРНЫЙ ВАРИАНТ\n")

	for i in range(pass_len):
		result_t += chars[rand(0, len(chars)-1)]
	return result_t

def pattern1():
	lets_big 		= "BCDFGHJKLMNPRSTVWXZ"
	lets_small 		= "bcdfghjklmnprstvwxz"
	lets_small_vo 	= "aeiouy"
	symbols = "#$_[].=+-|"
	result = getRandomChar(lets_big)+getRandomChar(lets_small_vo)+getRandomChar(lets_small)+getRandomChar(lets_big)+getRandomChar(lets_small_vo)+getRandomChar(lets_small)+str(rand(1000,9999))
	while(True):
		text = "Использовать спец. символы?\n1 - Да\n2 - Нет"
		print(text)
		value = int(input())
		if value == 1:
			while (True):
				text1 = "Сколько спец. символов нужно использовать? ( 1 - 4 ) "
				print(text1)
				try:
					value1 = int(input())
					if value1 >= 1 and value1 <= 4:
						for i in range(value1):
							result += getRandomChar(symbols)
						break
					else:
						system('cls||clear')
				except:
					system('cls||clear')
		elif value == 2:
			break
		else:
			system('cls||clear')

		break
				
	
	return result

main()
