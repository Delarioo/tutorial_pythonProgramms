from os import system

class sys:

	#Ставит программу на паузу (Windows/*nix)
	#Аргументы: nil
	#Возвращает: nil
	def pause():
		system('pause||read -s -n 1 -p "Press any key to continue . . ."')

	#Выводит текст по шаблону
	#Аргументы: text - передаваемый текст; head - Заголовок (По умолчанию program); version - Версия продукта (по умолчанию 1.0);
	#useCellar - использовать закрывающие звезды или нет. (По умолчанию True); pause - Поставить программу на паузу после вывода текста
	#Возвращает: nil
	def p(text, head='Program',version='1.0', useCellar=True, pause=False):
		system('cls||clear')
		print(f'{head} [{version}]')
		print('***************\n\n')
		print(text+'\n\n')
		if useCellar:
			print('***************')
		if pause:
			sys.pause()



class math:

	#Выполняет вычисления внутри пределов
	#Аргументы: input - вычисление; min - левый предел; max - правый предел
	#Возвращает: вычисление, внутри предела или предел
	def Clamp(input,min,max):
		if input > max:
			return max
		elif input < min:
			return min
		else:
			return input


	#
	#
	#



'''CHANGELOG

[20210624]
-Начало постройки ядра
-Организация классов sys и math
-math.Clamp - добавлено
-sys.p - изменено
	*Добавление автопаузы
	*Добавление настройки использования подвальных звезд
-sys.pause - изменено
	*Добавление поддержки Linux (NotTested)

'''