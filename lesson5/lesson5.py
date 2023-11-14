#функции - формула как в математике

#def -указывает что мы будем создавать функцию
#square -название функции(может быть каким угодно vasya petya)
#a, b - параметры функции (название может иметь любое)
#square(10, 33) square(22, 55) - вызов функций (внутри значения параметров)
#
# def square(a, b):
#     print(a*b)
#
# square(10, 33)
# square(22, 55)

# def person(hair, eyes, height, gender):
#     print(f'{hair}\n'
#           f'{eyes}\n'
#           f'{height}\n'
#           f'{gender}')
#
# person('black hair', 'eyes brown',184, 'male')
# person('white hair','blue eyes', 169, 'female')

# #return - возвращение действий, действие функции всегда строго пишется через return
# def family(father, monther, brother, sister, dauther, soon):
#     return (f'Папа-{father}\n'
#             f'Мама-{monther}\n'
#             f'Брат-{brother}\n'
#             f'Сестра-{sister}\n'
#             f'Дочь-{dauther}\n'
#             f'Сын-{soon}')
# print(family(father='Паша', monther='Ольга',
#              brother='Витя',
#              sister='Марина', dauther='Карина', soon='Владимир'))

##параметр по умолчанию
# def family(father, monther, brother, sister, dauther, soon='Петруха'):
#     return (f'Папа-{father}\n'
#             f'Мама-{monther}\n'
#             f'Брат-{brother}\n'
#             f'Сестра-{sister}\n'
#             f'Дочь-{dauther}\n'
#             f'Сын-{soon}')
# print(family(father='Паша', monther='Ольга',brother='Витя',sister='Марина', dauther='Карина', soon='Maksim'))
#

# #создание кортежа с помощью функций *args/ args помогает создать бесконечное кол во аргументов
# def family(*name):
#     return name
# print(family('Lena', 'Pasha', 'Dannil', 'Sharik', 'Barsik', 'Egor'))

# #Создание словаря с помощью функций
# def menu(**kwargs):
#     return kwargs
# print(menu(Завтрак="Яйца", Обед='Борщ с салом', Ужин='Пельмени'))