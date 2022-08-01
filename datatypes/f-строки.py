# f-строки
# https://python-scripts.com/f-strings

# например:
# name = 'oleg'
# lang = 'python'
# my_str = f'Hello, my name is {name.capitalize()}, i know {lang} a bit'
# print(my_str)

# можно разделять периоды чисел любым разделителем

# year_salary = 10000000
# print(f"Годовая зарплата: ${year_salary :,}")

# можно представлять числа с округлением до нужного количества знаков

# pi_value = 3.141592653589793
# print(f"Число Пи: {pi_value :.2f}")

# и много чего еще:
# https://saralgyaan.com/posts/f-string-in-python-usage-guide

# еще один пример:

# planet = 'Pluto'
# pluto_mass = 1.303 * 10**22
# earth_mass = 5.9722 * 10*24
# population = 52910390

# print(f"{planet} weights about {pluto_mass:.2e} killograms ({pluto_mass / earth_mass :.3%} of Earth mass). It is home to {population:,} Plutonians.")
