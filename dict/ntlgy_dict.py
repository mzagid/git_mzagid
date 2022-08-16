java_dict = {"title":"Java-разработчик с нуля", 
						 "duration":11, 
						"mentors":["Павел Дерендяев", "Алексей Яковлев", "Дмитрий Гордин", "Сергей Сердюк", "Анатолий Корсаков", "Вадим Ерошевичев", "Алексей Фомичев", "Филипп Воронов"],
						"price":0}

web_dict = {"title":"Web-разработчик с нуля",
					 "duration":19,
					 "mentors":["Николай Лопин", "Алёна Батицкая", "Алексей Дацков", "Александр Беспоясов", "Евгений Корытов", "Алексей Кулагин", "Ильназ Гильязов", "Владимир Языков", "Владимир Чебукин", "Эдгар Нуруллин", "Александр Дудинский"]}

frontend_dict = {"title":"Frontend-разработчик с нуля",
								"duration":13,
								"mentors":["Ильназ Гильязов", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алёна Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер"]}

java_set = set(java_dict["mentors"])
web_set = set(web_dict["mentors"])
frontend_set = set(frontend_dict["mentors"])
# print(type(java_set))
# print(java_set)

# print(web_set & frontend_set)
# print(len(web_set & frontend_set))

# all_set = java_set | web_set | frontend_set
# print(len(all_set))
# print(all_set)

# print()
# java_list = java_dict["mentors"]
# web_list = web_dict["mentors"]
# frontend_list = frontend_dict["mentors"]
# all_list = java_list + web_list + frontend_list
# print(len(all_list))
# print(all_list)
# print()
# print(len(set(all_list)))
# print(set(all_list))

# print("Web - frontend")
# print(web_set - frontend_set)
# print("frontend - Web")
# print(frontend_set - web_set)

# # симметрическая разность
# print("Web ^ frontend")
# print(web_set ^ frontend_set)
# print("frontend ^ Web ^ java")
# print(frontend_set ^ web_set ^ java_set)
# print()
print((web_set - frontend_set) | (frontend_set - web_set))

# test_1 = {1, 2, 3}
# test_2 = {2, 1}
# print(test_1 ^ test_2)
# if len(test_1 & test_2) == len(test_2) & len(test_1 & test_2) == len(test_1):
# 	print("Равны")
# else:
# 	print("Не равны")

print("Пересечение")
print(web_set.intersection(frontend_set, java_set))
print(web_set.intersection(frontend_set))
print("Объединение")
print(web_set.union(frontend_set, java_set))
print("Разность web - front")
print(web_set.difference(frontend_set, java_set))
print("Разность front - web")
print(frontend_set.difference(web_set))
print("Симметрическая разность web - front")
# print(web_set.symmetric_difference(frontend_set, java_set))
print(web_set.symmetric_difference(frontend_set))

print("Длинная операция с множествами")
print(web_set.difference(frontend_set).union(frontend_set.difference(web_set)))




# test_set = set()
# test_set = {1, "test"}
# print(type(test_set))


courses_list = [java_dict, frontend_dict, web_dict]

max_count = 0
course_id = None
for id, course in enumerate(courses_list):
	mentors_count = len(course["mentors"])
	# print(f'На курсе {course["title"]} {mentors_count}')
	if mentors_count > max_count:
		max_count = mentors_count
		course_id = id

# print(f'Самый крутой курс {courses_list[course_id]["title"]}, потому что на нем {max_count} преподавателей')

# for k in java_dict:
# 	print(k)
# 	print(java_dict[k])

# for k, v in java_dict.items():
# 	print(k, v)

# if "price" in java_dict.keys():
# 	print(java_dict["price"])
# else:
# 	print("Нет такого ключа!")

# result = java_dict.get("price")
# if result == None:
# 	print("Нет такого ключа!")

# вот что делает функция get()
# if "price" in java_dict.keys():
# 	print(java_dict["price"])
# else:
# 	print(None)

# ключи и значения словаря
# print(type(java_dict.keys()))
# print(java_dict.keys())
# java_keys = list(java_dict.keys())
# print(java_keys)

# print(type(java_dict.values()))
# print(java_dict.values())
# java_values = list(java_dict.values())
# print(java_values)

del(java_dict["price"])
# print(java_dict)

# java_dict.setdefault("price", None)
# print(java_dict)
# java_dict["price"] = 0
# # java_dict.setdefault("price", 0)
# print(java_dict)

cpp_dict = {"title":"C++ разработчик с нуля"}
# setdefault
cpp_dict.setdefault("mentors", [])
# либо не setdefault и пишем руками
if "mentors" not in cpp_dict.keys():
	cpp_dict["mentors"] = []
cpp_dict["mentors"].append("Преподаватель 1")
# print(cpp_dict)

# courses_list = [
# 	{
# 		"title":"Java-разработчик с нуля", 
# 		"mentors": ["Павел Дерендяев", "Алексей Яковлев", "Дмитрий Гордин", "Сергей Сердюк", "Анатолий Корсаков", "Вадим Ерошевичев", "Алексей Фомичев", "Филипп Воронов"],
# 		"duration": 11
# 	},
# 	{
# 		"title":"Веб-разработчик с нуля",
# 		"mentors": ["Николай Лопин", "Алёна Батицкая", "Алексей Дацков", "Александр Беспоясов", "Евгений Корытов", "Алексей Кулагин", "Ильназ Гильязов", "Владимир Языков", "Владимир Чебукин", "Эдгар Нуруллин", "Александр Дудинский"],
# 		"duration": 19
# 	},
# 	{
# 		"title":"Frontend-разработчик с нуля",
# 		"mentors": ["Ильназ Гильязов", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алёна Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер"],
# 		"duration": 13
# 	}