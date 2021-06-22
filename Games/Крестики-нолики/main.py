"""

0|1|2
3|4|5
6|7|8

_|_|_ 1
_|_|_ 2
_|_|_ 3

A B C
"""
version = '1.0 ALPHA'
from os import system
from bot import bot
def main():
	print(game())

def game():
	cell = [0,0,0,0,0,0,0,0,0]
	xx = 0
	while (xx < 5): #НЕ ЗАБЫТЬ ЗАМЕНИТЬ НА 5
		answ = 0;
		p(getGrid(cell)+'\n\nВаш ход!\nВыберите ячейку\n1 - A1\t2 - B1\t3 - C1\n4 - A2\t5 - B2\t6 - C2\n7 - A3\t8 - B3\t9 - C3')

		#Проверяет победителя
		if checkWinner(cell) == 1:
			return 'ПОБЕДИТЕЛЬ'
		elif checkWinner(cell) == 2:
			return 'ПРОИГРАВШИЙ'
		try:
			answ = int(input("Введите число (1-9): "))-1
			if (answ > 10 or answ < 0):
				print('Вы ввели неверное число!')
				pause()
				continue
			if cell[answ] != 0:
				continue
		except:
			print('Вы ввели неверное число!')
			pause()
			continue

		cell[answ] = 1
		bbot = bot(cell)
		if bbot != -1:
			cell[bbot] = 2
		else:
			'БОТ СДАЛСЯ СУКА'
		xx+=1


		#Возвращает ничью, если все клетки заполнены
	return 'НИЧЬЯ'


def getGrid(cell):
	r=['','','','','','','','','',]
	for i in range(len(cell)):
		if cell[i] == 0:
			r[i] = '_'
		elif cell[i] == 1:
			r[i] = 'x'
		elif cell[i] == 2:
			r[i] = 'o'
		else:
			r[i] = '_'
	return r[0]+'|'+r[1]+'|'+r[2]+' 1\n'+r[3]+'|'+r[4]+'|'+r[5]+' 2\n'+r[6]+'|'+r[7]+'|'+r[8]+' 3\n\nA B C'

#Перебирает все возможные выигрышные комбинации и возвращает победителя, если он есть.
def checkWinner(cell):
	comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for j in comb:

		if (cell[j[0]] == cell[j[1]] == cell[j[2]] == 1) or (cell[j[0]] == cell[j[1]] == cell[j[2]] == 2):
			return cell[j[0]]

def pause():
	system('pause')

def p(text):
	system('cls||clear')
	print(f'КРЕСТИКИ-НОЛИКИ [{version}]')
	print('***************\n\n')
	print(text)
	print('\n\n***************')


if __name__ == '__main__':
	main()


'''
[CHANGELOG]
[1.0a]
-Создание программы, подведение к рабочему состоянию
-Создание бота для одиночной игры
-Создание и отработка логики бота
-Создание интерфейса для работы
-Чистка от багов
'''