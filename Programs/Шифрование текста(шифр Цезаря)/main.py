VERSION = '1.0 RUS'

from core import sys

def main():
	russian = 'абвгдеёжсийклмнопрстуфхцчшщъыьэюя'

	p('Шифр Цезаря подразумивает смещение букв вперед на 1-32 позиций, что делает зашифрованным. \nШифр Цезаря считается одним из самых простых шифров', pause=True)
	p('Сначала введите текст, а затем укажите число (1-32) для смещения букв', pause=True)

	
	text = []
	offset = 1
	while(True):
		p('')
		try:
			text = list(input('\nУкажите текст (Только русские буквы, цифры и знаки): ').lower())
			if len(text) < 1:
				raise Exception('')
			break
		except:
			p('Введен неправильный текст! Повторите попытку', pause=True)
			continue
	while(True):
		p('')
		try:
			offset = int(input('\nУкажите число сдвига (1-32): '))
			if offset > 32 or offset < 1:
				raise Exception('')
			break
		except:
			p('Вы указали неверное число! Диапозон числа от 1 до 32.\nПовторите попытку',pause=True)
			continue
	# каждую букву введенной строки сравниваем с алфавитом, а затем делаем смещение
	for i in range(len(text)):
		for j in range(len(russian)):
			if text[i] == russian[j]:
				if j + offset <= len(russian)-1:
					text[i] = russian[j+offset]
					break
				else:
					text[i] = russian[j+offset-len(russian)-1]
					break

	result = ''.join(text)
	p(f'Ваш текст был сдвинут на {offset} букв(ы). \nТеперь он выглядит так: {result}')



def p(text, cellar=False, pause=False):
	sys.p(text, 'ШИФР ЦЕЗАРЯ', useCellar=cellar, pause=pause,version=VERSION)

if __name__ == '__main__':
	main()


'''
[changelog]
[1.0]
-Создание программы
-Построение основных алгоритмов
-Исправление багов

'''