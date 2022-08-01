# СПИСКИ (list)

# списки (list) это структура данных для упорядоченного хранения объектов различных типов.
# является изменяемым типом данных, в отличие от всех предыдущих.
# список инициализируется при помощи [ ], элементы в списке разделяются запятыми.

# month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']

# income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]

# income_by_months = [['Jan', 13000], ['Feb', 14000], ['Mar', 14300], ['Apr', 15000], ['May', 13800], ['Jun', 13000], ['Jul', 14900], ['Aug', 15200], ['Sep', 15300]]

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

# все операции со списками:
# https://docs.python.org/3/tutorial/datastructures.html