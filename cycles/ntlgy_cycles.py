# ЦИКЛ WHILE

# money = 5
# while money > 0:
#   money -= 1 # 'x -=' - тоже самое, что и 'x = x - 1'
#   print('Денег осталось: ', money)

# print('Денег больше нет.')

# x = 5
# while x != 0:
#   x -= 1
#   print(x)

# x = 7
# while x != 0:
#   if x % 2 == 0:
#     print(x, '- четное число')
#   else:
#     print(x, '- нечетное число')
#   x -= 1

# напишем программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введеных чисел.

# sum_ = 0
# a = ""
# while a != 0:
#   a = int(input())
#   sum_ += a

# print(sum_)

# ЦИКЛ FOR'

# итерация по строкам
# company_name = 'Netology'
# # мы сами задаем имя переменной в которую будут последовательно помещаться каждый элемент нашего объекта
# for letter in company_name:
#   print(letter)
  # print(f'*{letter.upper()}*', end='')

# у нас есть фургон, в котором мы перевозим грузы. установлено ограничение на максимальный вес груза в 100 кг. необходимо произвести фильтрацию данных грузов.

# items = [1, 5, 76, 12, 123, 333, 5, 6, 7]
# ok_items = []
# for item in items:
#   print('Груз весит', item, 'килограмм')
#   if item <= 100:
#     ok_items.append(item)
#     print('Груз прошел проверку')
#   else:
#     print('Груз слишком большой')
# print(ok_items)

# выведем информацию о компаниях, которые хранятся во вложенных списках в виде:
# company's capitalization is ***

# companies_capitalization = [
#   ['Orange', 1.3],
#   ['Maxisoft', 1.5],
#   ['Headbook', 0.8],
#   ['Nicola', 2.2]
# ]
# for company in companies_capitalization:
#   # print(company)
#   print(f"{company[0]}'s capitalization is {company[1]}")

# мы можем распаковать элементы прямо в списке 

# companies_capitalization = [
#   ['Orange', 1.3],
#   ['Maxisoft', 1.5],
#   ['Headbook', 0.8],
#   ['Nicola', 2.2]
# ]
# for company_name, cap in companies_capitalization:
#   print(f"{company_name}'s capitalization is {cap}")

# посчитаем сумму элементов по главной диагонали квадратной матрицы

# data = [
#   [13, 25, 23, 34],
#   [45, 32, 44, 47],
#   [12, 23, 33, 95],
#   [13, 53, 34, 35],
# ]

# sum_ = 0
# index = 0
# for row in data:
#   print(row)
#   sum_ += row[index]
#   index += 1
# print(sum_)

# BREAK, CONTINUE, PASS
# phrase = '640 кб должно хватить для любых задач. Билл Гейтс (по легенде)'

# for letter in phrase:
#   if letter == ' ':
#     break
#   print(letter, end='')

# for letter in phrase:
#   if letter == ' ':
#     continue
#   print(letter, end='')

# for letter in phrase:
#   if letter == ' ':
#     pass
#   print(letter, end='')