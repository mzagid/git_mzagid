# ЯВНОЕ ПРИВЕДЕНИЕ ТИПОВ

# тип данных можно принудительно изменить функциями int(), float(), bool(), str():

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

# но существует и неявное преобразование, например:

# print(2 + True)
# print(20 / 5)