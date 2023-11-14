#
# countries = {
#     'kg': ['red', 'yellow'],
#     'ru': ['white', 'red', 'blue'],
#     'us': ['blue', 'red', 'white'],
#     'tr': ['red', 'white'],
#     'it': ['green', 'white', 'red'],
#     'uk': ['blue', 'yellow'],
#     'abh': ['green', 'red', 'white']
# }
#
# while True:
#     colors = list(map(str, input('Введите цвета через пробел: ').split()))
#
#     found = 0
#     for keys, values in countries.items():
#         if len(values) < len(colors):
#             continue
#         count = 0
#         for color in values:
#             if color in colors:
#                 count += 1
#         if count == len(colors):
#             print(keys)
#             found += 1
#
#     if found == 0:
#         print('Флаг с такими цветами не найден')
#
#     yes = 0
#     while True:
#         cont = str(input('Хотите продолжить? y/n '))
#         if cont.lower() == 'n':
#             break
#         if cont.lower() == 'y':
#             yes += 1
#             break
#     if yes == 1:
#         continue
#     else:
#         break
#
#     # # INAI = {
# # #     'address': 'Toktogula 175',
# # #     'courses': ['Android', 'Backend', 'Frontend'],
# # #     'bag': {'fails', 'errors', 'stack'}
# # # }
# # # #delete bag
# # # del INAI['bag']
# # # INAI['address'] = 'Тимирязева 74'
# # # INAI['telefone'] = '0555111222'
# # # INAI['instagram'] = '@inai'
# # # INAI['courses'].append('HTML CSS')
# # # courses = ['php', 'laravel']
# # # INAI['courses'].extend(courses)
# # #
# # # for keys, values in INAI.items():
# # #     print(f'{keys}-{values}')
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # Создаем словарь с цветами флагов для разных стран
# # countries = {
# #     'kg': {'red', 'yellow'},
# #     'ru': {'white', 'red', 'blue'},
# #     'fr': {'blue', 'white', 'red'},
# #     'us': {'red', 'white', 'blue'},
# # }
# #
# # # Функция для определения страны по цветам
# # # def find_country_by_colors(user_colors):
# # #     for country, flag_colors in countries.items():
# # #         if user_colors == flag_colors:
# # #             return country
# # #     return None
# # #
# # # # # Основной цикл программы
# # # # while True:
# # # #     user_input = input("Введите цвета через запятую: ")
# # # #     user_colors = set(user_input.split(','))
# # # #
# # # #     matched_country = find_country_by_colors(user_colors)
# # # #
# # # #     if matched_country:
# # # #         print(f"Ваш ввод соответствует флагу страны с кодом '{matched_country}'.")
# # # #     else:
# # # #         print("Нет совпадений с флагами из нашего списка.")
# # # #
# # # #     choice = input("Хотите продолжить? (y/n): ")
# # # #     if choice.lower() != 'y':
# # # #         break
# # # #
# # #
# # # #
# # # # ksla = {
# # # #     'address': 'Toktogula 175',
# # # #     'courses': ['Android', 'Backend', 'Frontend'],
# # # #     'bag': {'fails', 'errors', 'stack'}
# # # # }
# # # #
# # # # # print('courses --> ', type(ksla['courses']))
# # # # # print('bag --> ', type(ksla['bag']))
# # # #
# # # # del ksla['bag']
# # # # ksla['address'] = ['Chui 180a', 'Maksima Gorkogo 18']
# # # # ksla['contacts'] = ['+996 (312) 39-20-93', 'ksla.kg']
# # # # ksla['courses'].append('Python')
# # # # ksla['courses'].append('JavaScript')
# # # # ksla['courses'].append('PHP')
# # # #
# # # # for keys, values in ksla.items():
# # # #     # print(f'{keys} --> {values}')
# # # #     print(f'{keys} --> {values}')
# # # #
# # # #
# # # #
# # # #
# # #
countries = {
    'kg': {'red', 'yellow'},
    'ru': {'white', 'red', 'blue'},
    'us': {'blue', 'red', 'white'},
    'tr': {'red', 'white'},
    'it': {'green', 'white', 'red'},
    'uk': {'blue', 'yellow'},
    'abh':{'green','red','white'}
}
while 1:
    colors = str(input("Введите цвета: "))
    colors = colors.split()
    a = []
    # items  делает словарь  парный список
    for k, v in countries.items():
        domen = True
        for c in colors:
            if c not in v:
                domen = False
        if domen == True:
            a.append(k)

    if len(a)==0:
        print('Домена нет')
    else:
        for i in a:
            print(i)

    exit = str(input('Хотите продолжить? y/n '))
    if exit == 'y':
         continue
    else:
       break