"""
0|1|2
3|4|5
6|7|8
"""

from random import randint as rand

# Обработчик логики противника.
# Аргумент: (list) Игровое поле;
# Возвращает: int (1-9) - ячейка поля, которую бот выбрал

def bot(cell):
	a,b = 4,4
	diagonals = [0,2,6,8]
	vertical = [1,3,5,7]

	#Анализируем поле и прописываем всевозможные исходы

	#заполняет центр, если он свободен
	if cell[4] == 0:
		return 4
	# АТАКА
	'''
	0|_|_
	_|0|_
	_|_|o
	'''		
	if (cell[4]==2 and cell[0]==2) and cell[8] == 0:
		return 8
	elif (cell[4]==2 and cell[2]==2) and cell[6] == 0:
		return 6
	elif (cell[4]==2 and cell[6]==2) and cell[2] == 0:
		return 2
	elif (cell[4]==2 and cell[8]==2) and cell[0] == 0:
		return 0
	'''			
	o|0|0	0|0|o
	_|_|_   _|_|_
	_|_|_   _|_|_
	'''	
	if (cell[0]==2 and cell[1]==2 and cell[2]==0):
		return 2
	elif (cell[3]==2 and cell[4]==2 and cell[5]==0):
		return 5
	elif (cell[6]==2 and cell[7]==2 and cell[8]==0):
		return 8
	elif (cell[1]==2 and cell[2]==2 and cell[0]==0):
		return 0
	elif (cell[4]==2 and cell[5]==2 and cell[3]==0):
		return 3
	elif (cell[7]==2 and cell[8]==2 and cell[6]==0):
		return 6		

	'''			
	0|_|_	o|_|_
	0|_|_   0|_|_
	o|_|_   0|_|_
	'''

	if (cell[0]==2 and cell[3]==2 and cell[6]==0):
		return 6
	elif (cell[1]==2 and cell[4]==2 and cell[7]==0):
		return 7
	elif (cell[2]==2 and cell[5]==2 and cell[8]==0):
		return 8
	elif (cell[3]==2 and cell[6]==2 and cell[0]==0):
		return 0
	elif (cell[4]==2 and cell[7]==2 and cell[2]==0):
		return 2
	elif (cell[5]==2 and cell[8]==2 and cell[3]==0):
		return 3

	'''			
	0|o|0	0|_|_
	_|_|_   o|_|_
	_|_|_   0|_|_
	'''
	if (cell[0]==2 and cell[2]==2 and cell[1]==0):
		return 1
	elif (cell[3]==2 and cell[5]==2 and cell[4]==0):
		return 4
	elif (cell[6]==2 and cell[8]==2 and cell[7]==0):
		return 7
	elif (cell[0]==2 and cell[6]==2 and cell[3]==0):
		return 3
	elif (cell[1]==2 and cell[7]==2 and cell[4]==0):
		return 4
	elif (cell[2]==2 and cell[8]==2 and cell[5]==0):
		return 5




	# ЗАЩИТА
	'''
	x|_|_
	_|x|_
	_|_|0
	'''		
	if (cell[4]==1 and cell[0]==1) and cell[8] == 0:
		return 8
	elif (cell[4]==1 and cell[2]==1) and cell[6] == 0:
		return 6
	elif (cell[4]==1 and cell[6]==1) and cell[2] == 0:
		return 2
	elif (cell[4]==1 and cell[8]==1) and cell[0] == 0:
		return 0

	'''			
	x|x|0	0|x|x
	_|_|_   _|_|_
	_|_|_   _|_|_
	'''	
	if (cell[0]==1 and cell[1]==1 and cell[2]==0):
		return 2
	elif (cell[3]==1 and cell[4]==1 and cell[5]==0):
		return 5
	elif (cell[6]==1 and cell[7]==1 and cell[8]==0):
		return 8
	elif (cell[1]==1 and cell[2]==1 and cell[0]==0):
		return 0
	elif (cell[4]==1 and cell[5]==1 and cell[3]==0):
		return 3
	elif (cell[7]==1 and cell[8]==1 and cell[6]==0):
		return 6		

	'''			
	x|_|_	0|_|_
	x|_|_   x|_|_
	0|_|_   x|_|_
	'''

	if (cell[0]==1 and cell[3]==1 and cell[6]==0):
		return 6
	elif (cell[1]==1 and cell[4]==1 and cell[7]==0):
		return 7
	elif (cell[2]==1 and cell[5]==1 and cell[8]==0):
		return 8
	elif (cell[3]==1 and cell[6]==1 and cell[0]==0):
		return 0
	elif (cell[4]==1 and cell[7]==1 and cell[2]==0):
		return 2
	elif (cell[5]==1 and cell[8]==1 and cell[3]==0):
		return 3

	'''			
	x|0|x	x|_|_
	_|_|_   0|_|_
	_|_|_   x|_|_
	'''
	if (cell[0]==1 and cell[2]==1 and cell[1]==0):
		return 1
	elif (cell[3]==1 and cell[5]==1 and cell[4]==0):
		return 4
	elif (cell[6]==1 and cell[8]==1 and cell[7]==0):
		return 7
	elif (cell[0]==1 and cell[6]==1 and cell[3]==0):
		return 3
	elif (cell[1]==1 and cell[7]==1 and cell[4]==0):
		return 4		
	elif (cell[2]==1 and cell[8]==1 and cell[5]==0):
		return 5

	#--ПРОЧИЕ ВАРИАНТЫ--#
	#Заполняет все свободные углы
	for i in diagonals:
		if cell[i] != 0:
			continue
		else: 
			return i
	#Заполняет все вертикали
	for i in vertical:
		if cell[i] != 0:
			continue
		else:
			return i
	return -1

	#-------------------------------

