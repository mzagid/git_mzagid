# ПРОСТЫЕ ТИПЫ ДАННЫХ

# my_integer = 10
# print(type(my_integer))

# my_float = 5.5
# print(type(my_float))

# my_string = 'Hello, world!'
# print(type(my_string))

# my_bool = True
# my_bool = False
# print(type(my_bool))

# ЯВНОЕ ПРИВЕДЕНИЕ ТИПОВ

# to_int = int('42')
# print(to_int)
# print(type(to_int))

# to_int_2 = int(True)
# print(to_int_2)
# print(type(to_int_2))

# to_float = float('42.42')
# print(to_float)
# print(type(to_float))

# to_str = str(42.42)
# print(to_str)
# print(type(to_str))

# to_str2 = str(True)
# print(to_str2)
# print(type(to_str2))

# to_bool = bool(42)
# print(to_bool)
# print(type(to_bool))

# to_bool_2 = bool(0)
# print(to_bool_2)
# print(type(to_bool_2))

# to_bool_3 = bool('some_string')
# print(to_bool_3)
# print(type(to_bool_3))

# to_bool_4 = bool('')
# print(to_bool_4)
# print(type(to_bool_4))

# НЕЯВНОЕ ПРЕОБРАЗОВАНИЕ ТИПОВ

# print(2 + True)
# print(20 / 5)

# РАБОТА СО СТРОКАМИ
# Строки можно создавать одинарными, двойными или тройными ковычками

# my_string = 'Hello, world!'
# my_string_2 = "Hello, world!"

# my_string = 'Hello, \nWorld!'
# print(my_string)

# multiline_string = """В такой "строке" мы можем
# 'использовать' все."""
# print(multiline_string)

# ДЕЙСТВИЯ НАД СТРОКАМИ

# сравнение строк

# print('a' > 'b')
# print('a' > 'B')
# print('abc' > 'aba')

# конкатенация (сложение строк)

# s1 = 'spam '
# s2 = 'eggs'
# print(s1 + s2)

# умножение строки на число

# print('**' * 5)

# help(str)

# my_string = 'HELLO world!'

# # приведение к верхнему регистру
# # print(my_string.upper())
# # new_string = my_string.upper()
# # print(new_string)

# # исходная строка никак не меняется!
# # print(my_string)

# # # приведение к нижнему регистру
# # print(my_string.lower())

# # # первая буква строки в верхнем регистре
# # print(my_string.capitalize())

# # # первая буква каждого слова в верхнем регистре
# # print(my_string.title())

# # заменяем подстроку в строке
# print(my_string.replace('HELLO', 'Goodbye'))

# метод find() ищет подстроку в строке и возвращает индекс первого элемента найденной подстроки.
# если подстрока не найдена, то возвращает -1.
# s = 'red blue orange white blue'
# print(s.find('b'))
# print(s.find('blue'))

# определяем длину строки
# print(len.(my_sting))

# проверка вхождения подстроки в строку
# my_string = 'Hello World'
# target_string = 'World'

# if target_string in my_string:
#   print('Найдено')
# else:
#   print('Не найдено')
# print(target_string in my_string)
# print(target_string not in my_string)

# f-строки
# https://python-scripts.com/f-strings

# name = 'oleg'
# lang = 'python'
# my_str = f'Hello, my name is {name.capitalize()}, i know {lang} a bit'
# print(my_str)

# Можно разделять периоды чисел любым разделителем

# year_salary = 10000000
# print(f"Годовая зарплата: ${year_salary :,}")

# Можно представлять числа с округлением до нужного количества знаков

# pi_value = 3.141592653589793

# print(f"Число Пи: {pi_value :.2f}")

# И много чего еще
# https://saralgyaan.com/posts/f-string-in-python-usage-guide

# planet = 'Pluto'
# pluto_mass = 1.303 * 10**22
# earth_mass = 5.9722 * 10*24
# population = 52910390

# print(f"{planet} weights about {pluto_mass:.2e} killograms ({pluto_mass / earth_mass :.3%} of Earth mass). It is home to {population:,} Plutonians.")

# ИНДЕКСАЦИЯ И СРЕЗЫ

# my_string = 'Hello World'

# print(my_string[0])

# # print(my_string[100])

# print(my_string[-5])

# print(my_string[3:8])

# print(my_string[1:8:2])

# print(my_string[::-1])

# т.к. строки являются неизменяемым типом, то нельзя перезаписать какой-то отдельный символ или срез в строке.

# my_string[-1] = '!'

# СПИСКИ (list)

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]

income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]

# индексация элементов в списке
# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# print(month_list[0])
# print('--------------')
# print(month_list[-1])
# print('--------------')
# print(month_list[-4])

# срезы
# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# print(month_list[1:3])
# print('--------------')
# print(month_list[-8:-6])
# print('--------------')
# print(month_list[2:])
# print('--------------')
# print(month_list[:3])
# print('--------------')
# print(month_list[::2])
# print('--------------')
# print(month_list[4:8:3])
# print('--------------')
# print(month_list[::-1])

# можно обращаться к любому уровню вложенности
# income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]
# print(income_by_months[0][0])

# изменение списков
# income_by_months[0][1] = 13100
# print(income_by_months)

# можем заменять сразу срез
# income_by_months[:2] = [['Jan', 13200], ['Feb', 13900]]
# print(income_by_months)

# можем складывать списки
# income_by_months_2 = [['Nov', 15400], ['Dec', 17000]]
# income_by_months = income_by_months + income_by_months_2
# print(income_by_months)

# удаляем элемент по индексу
# del(income_by_months[-1])
# print(income_by_months)

# # удаляем элемент по значению
# month_list.remove('Sep')
# print(month_list)

# # добавляем элемент в конец списка
# income_by_months.append(['Dec', 17000])
# print(income_by_months)

# # добавляем элемент по нужному индексу
# income_list.insert(2, 1111111)
# print(income_list)

# считаем количество вхождений элемента в список
# print(income_list.count(13000))

# узнаем индекс элемента в списке (только первое вхождение!)
# print(income_list.index(13000))
# print(income_list.index(13000, 1))

# разворачиваем список
# month_list.reverse()
# print(month_list)

# узнаем длину списка
# print(len(income_list))

# какие длины у этих списков?
# a = [1, 2, 3]
# b = [1, [2, 3]]
# c = []
# d = [1, 2, 3] [1:]
# print(d)

# сумма элементов в списке
# print(sum(income_list))

# # максимальный элемент элементов
# print(max(income_list))

# # минимальный элемент элементов
# print(min(income_list))

# сортировка по возрастанию
# print(sorted(income_list)

# изменить порядок сортировки
# print(sorted(income_list, reverse=True))

# сортировка строк по алфавиту
# print(sorted(month_list))

# income_list.sort() # метод sort для сортировки

# методы строк связанные со списками
# queries_string = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"

# # (!) преобразование строки в список (например, из CSV-файла)
# # print(queries_string.split(','))

# # преобразование списка в строку
# print('!!!'.join(['Столбец 1', 'Столбец 2']))

# Методы изменяемых типов данных всегда меняют исходный объект а не создают новый!
# Методы неизменяемых типов данных всегда возвращают новый объект и не меняют исходный.
# (Методы - меняют исходный объект, функции - нет)

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# res = month_list.sort()
# print(res)
# print(month_list)

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# sorted(month_list) # функция sorted создает новый объект
# print(month_list)

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# res = sorted(month_list)
# print(res)
# print(month_list)

# в примере ниже переменная 'a' и 'b' указывают на один и тот же объект. В результате, при добавлении в 'b' очередного элемента этот элемент добавляется и в исходном листе 'a'. Это особенность всех изменяемых типов данных.

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)

# print(id(a))
# print(id(b))

# # создаем копию объекта
# a = [1, 2, 3]
# b = list(a)
# b.append(4)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# # создаем копию объекта (другой способ)
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# # создаем копию объекта (еще один способ)
# a = [1, 2, 3]
# b = a[:]
# b.append(4)
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# КОРТЕЖИ

# salary_tuple = (1000, 1200, 1300, 900, 800)
# print(type(salary_tuple))
# print(type(list(salary_tuple)))

# salary_tuple[0] = 500

# # кортеж из одного элемента задается так:
# one_el_tuple = ('one', )

# # без запятой получится строка
# print(type( ('one') ))

# ФУНКЦИЯ ZIP

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
# salaries_by_names = zip(month_list, income_list)
# print(salaries_by_names)
# print(list(salaries_by_names))

# # проверка вхождения
# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
# print('Jan' in month_list)