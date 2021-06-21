#### SETTINGS #######
					#
num_min = 	0		#	- Минимальное число
num_max = 	10		#	- Максимальное число
chance = 	3		#	- Количество попыток
					#
#####################

version = 	'1.0 [FINAL]'

from random import randint as rand
from os import system


def p(txt):
	system("cls||clear")
	print("GUESS THE NUMBER [ ver", version,']')
	print("***********************************\n")
	print(txt)

def pause():
	system('pause')

def main(min, max, chance):
	num_min = min
	num_max = max 
	chance = chance
	answ = int()
	number = rand(num_min,num_max)
	while(chance > 0):
		p(f'Напишите свое число от {num_min} до {num_max}:')
		try:
			answer = int(input())
			if answer >= num_min and answer <= num_max:
				answ = answer
			else:
				continue
		except ValueError:
			continue

		if answer == number:
			p('ВЫ УГАДАЛИ ЧИСЛО!')
			break
		else:
			chance -=1
			p(f'Ваше число не верно, повторите попытку! Попыток осталось: {chance}')
			pause()
	if chance == 0:
		p('ВЫ ПРОИГРАЛИ!')

if __name__ == '__main__':
	main(num_min,num_max,chance)



''' 
CHANGELOG
[1.0] [FINAL]
-Удаление лишнего кода
-Теперь число генерируется один раз за игру, а не при каждой попытке, от чего игра становится более простой, а
попытки начинают иметь значение

[0.1a]
-Создание программы
-Написание основого кода
-Добавление настроек в первых строках кода
-

'''