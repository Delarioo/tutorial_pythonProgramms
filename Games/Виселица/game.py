# SETTINGS
useStaticChance = False 	# Использование статических попыток игры, а не зависящих от количества букв
chance = 10					# Количество попыток (Должно быть больше нуля)
addToChances = 2			# Количество попыток, добавляемое к переменной, зависящей от количества букв (Количество букв + значение переменной = количество попыток)
# Extended settings
fileWords = 'words_example_ru.txt'
version = '1.0'

###########


from os import system
from random import randint


def main():
	russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
	# english = 'abcdefghijklmnopqrstuvwxyz-'
	usedsymbols = ''
	chances = 0
	table = loadWords()
	if table == 'GLOBAL_ERROR':
		return
	#Получаем случайное слово из списка
	word = str.lower(table[randint(0,len(table)-1)])
	# Создаем список символов на основе количества букв. Каждое значение равно '_'
	res = ['_' for i in range(0, len(word))] 
	# Получаем число символов слова
	symbols = len(word) 
	if useStaticChance:
		chances = chance
	else:
		chances = len(word)+addToChances
	# Цикл длится до тех пор, пока не закончатся количество попыток или не будут отгаданы все буквы
	while(chances != 0 and symbols !=0):
		#Введем локальные переменные
		#Создаем переменную и заполняем ее значениями списка символов угадываемого слова.
		xx = '' 
		for i in res:
			xx += i+' '
		# Угадана ли буква
		lucky = False 
		# Соответствует ли введеный символ отбору по правилам, указанным ниже
		isValid = False 
		# Использован ли символ ранее
		isUsed = False 

		p(f'Попыток: {chances}   Осталось букв: {symbols}\n Слово: {xx}')

		answer = str.lower(input("Ваша буква: "))
		# Если введено больше одной буквы, то ответом будет являться первая буква	
		if len(answer)>1: answer = answer[0] 
		# Проверка на соответствие русскому алфавиту или символу '-'
		for i in range(len(russian)):
			if answer == russian[i]:
				isValid = True
				break;
		#Если символ не входит в русский алфавит, то цикл While начинается заново
		if not isValid:
			print("Только русские буквы или символ '-'")
			pause()
			continue
		#Проверка на использованный ранее символ
		for i in range(len(usedsymbols)):
			if answer == usedsymbols[i]:
				isUsed = True
				break
		#Исли символ использован ранее, то цикл While начинается заново
		if isUsed:
			print(f"Вы уже использовали '{answer}'")
			pause()
			continue
		#Проверка на соответствие введенного символа символам слова
		for i in range(len(res)):
			if answer == word[i]:
				res[i] = answer
				lucky = True
				symbols -=1
		#Добавление символа к ранее введенным символам, для исключения повторного использования.
		usedsymbols +=answer
		#Если такого символа нет в слове, то отнимается попытка
		if not lucky:
			chances -=1
	if symbols == 0:
		pause()
		p(f'ВЫ ПОБЕДИЛИ! Слово: {word}')
	if chances == 0:
		p(f'ВЫ ПРОИГРАЛИ! Слово: {word}')
	
#Загрузка списка слов из файла
#Возвращает список или 'GLOBAL_ERROR'
def loadWords():
	table = list()
	try:
		table = [line.strip() for line in open(fileWords)]
		return table
	except FileNotFoundError:
		print('Файл не найден! Пожалуйста, укажите в настройках правильную базу слов.')
		return 'GLOBAL_ERROR'

#Шаблон вывода в консоль
def p(text):
	system('cls||clear')
	print(f'ВИСЕЛИЦА [{version}]\n\n********************\n\n')
	print(text)
#Пауза
def pause():
	#input('Нажмите Enter для продолжения...')
	system('pause')
#Запуск программы
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