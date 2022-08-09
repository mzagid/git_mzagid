person = 5
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]
for name, list_of_ingredients in cook_book:
    name = name.capitalize()
    print()
    print(f'{name}:')
    for ingredient_name, count, units in list_of_ingredients:
      count *= person
      print(ingredient_name, count, units)

# for i in cook_book:
#     print(f'\n{i[0].title()}:')
#     for j in i[1]:
#         print(f'{j[0]}, {j[1] * person}{j[2]}')

#######################################################

# условие задачи (задача №2): 
https://github.com/netology-code/py-homeworks-basic/tree/master/3.introduce_datatypes