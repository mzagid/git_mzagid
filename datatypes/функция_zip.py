# ФУНКЦИЯ ZIP

# Функция zip(list_1, list_2, ...) берёт на вход несколько списков/кортежей
# и создаёт из них специальный zip-объект состоящий из кортежей,
# такой, что первый элемент полученного объекта содержит кортеж из первых элементов всех списков-аргументов.

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
income_list = [13000, 14000, 14300, 15000, 13800, 13000, 14900, 15200, 15300]
salaries_by_names = zip(month_list, income_list)
print(salaries_by_names)
print(list(salaries_by_names))
