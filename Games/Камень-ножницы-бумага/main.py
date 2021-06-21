#### SETTINGS #######
					#
maxRes = 	7		# - Максимальный счёт
					#
#####################

version = 	'1.0 [FINAL]'

from random import randint as rand
from os import system


def p(txt):
	system("cls||clear")
	print("КАМЕНЬ-НОЖНИЦЫ-БУМАГА [ ver", version,']')
	print("***********************************\n")
	print(txt)

def pause():
	input("\nНажмите ENTER для продолжения!")
	input

def getResult(answ, num):
	if answ == num:
		return "Ничья", -1
	elif answ < num and not (answ == 1 and num == 3):
		return "Победа", 1
	elif answ > num and not (answ == 3 and num == 1):
		return "Поражение", 0
	elif answ == 3 and num == 1:
		return 'Победа', 1
	elif answ == 1 and num == 3:
		return 'Поражение', 0

def main(maxRes):

	answ = int()
	a = 0
	b = 0

	while(maxRes > a and maxRes > b):
		number = rand(1,3)
		p(f'СЧЕТ {a} | {b}\nВведите значение от 1 до 3:\n1 - Камень\n2 - Ножницы\n3 - Бумага')
		try:
			answer = int(input("Ответ: "))
			if answer >= 1 and answer <=3:
				answ = answer
			else:
				continue
		except ValueError:
			continue
		result, n = getResult(answ,number)
		p(result)
		if n == 1:
			a +=1
		elif n == 0:
			b +=1
		pause()
	if a > b:
		p('ВЫ ПОБЕДИЛИ!')
	else:
		p("ВЫ ПРОИГРАЛИ!")	


if __name__ == '__main__':
	main(maxRes)



''' 
CHANGELOG
[1.0 FINAL]
-Введение системы счета, теперь игру можно выиграть или проиграть.
-Введение настройки максимального счета

[0.2A]
-Доведение программы до рабочего состояния
-Теперь нельзя ввести число выше 3 и ниже 0
-Зацикливание игры

[0.1A]
-Создание программы, написание простого алгоритма игры

'''