# SETTINGS
useStaticChance = False 	# Использование статических попыток игры, а не зависящих от количества букв
chance = 0					# Количество попыток (Должно быть больше нуля)
addToChances = 2			# Количество попыток, добавляемое к переменной, зависящей от количества букв (Количество букв + значение переменной = количество попыток)
# Extended settings
fileWords = 'words.txt'
version = '1.0'

###########


from os import system
from random import randint


def main():
	russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
	usedsymbols = ''
	chances = 0
	table = loadWords()
	if table == 'GLOBAL_ERROR':
		return

	word = str.lower(table[randint(0,len(table)-1)])
	res = ['_' for i in range(0, len(word))]
	symbols = len(word)

	if useStaticChance:
		chances = chance
	else:
		chances = len(word)+addToChances

	while(chances != 0 and symbols !=0):
		xx = ''
		for i in res:
			xx += i+' '
		lucky = False
		isValid = False
		isUsed = False
		p(f'Попыток: {chances}   Осталось букв: {symbols}\n Слово: {xx}')
		answer = str.lower(input("Ваша буква: "))	
		if len(answer)>1: answer = answer[0] # Если введено больше одной буквы, то ответом будет являться первая буква

		for i in range(len(russian)):
			if answer == russian[i]:
				isValid = True
				break;
		if not isValid:
			print("Только русские буквы или символ '-'")
			pause()
			continue

		for i in range(len(usedsymbols)):
			if answer == usedsymbols[i]:
				isUsed = True
				break

		if isUsed:
			print(f"Вы уже использовали '{answer}'")
			pause()
			continue
		for i in range(len(res)):
			if answer == word[i]:
				res[i] = answer
				lucky = True
				symbols -=1

		usedsymbols +=answer

		if not lucky:
			chances -=1
	if symbols == 0:
		pause()
		p(f'ВЫ ПОБЕДИЛИ! Слово: {word}')
	if chances == 0:
		p(f'ВЫ ПРОИГРАЛИ! Слово: {word}')
	

def loadWords():
	table = list()
	try:
		table = [line.strip() for line in open(fileWords)]
		return table
	except FileNotFoundError:
		print('File not found!')
		return 'GLOBAL_ERROR'


def p(text):
	system('cls||clear')
	print(f'ВИСИЛИЦА [{version}]\n\n********************\n\n')
	print(text)

def pause():
	#input('Нажмите Enter для продолжения...')
	system('pause')

if __name__ == '__main__':
	main()

""" 
[CHANGELOG]
[1.0b]
-Замена вывода таблицы букв, представляющей слово, на отдельный текст, 
то есть теперь выводимое слово имеет формат не ['x', 'x','x'], а 'x_xx_xx'
-Теперь количество оставшихся букв не снимается, если игрок вводит несколько раз подряд одну и ту же правильную букву
-Игрок информируется о том, что он ввел один и тот же символ

[0.1]
-Создание программы, доведение до рабочего состояния
-Создание отдельного файла со словами


"""