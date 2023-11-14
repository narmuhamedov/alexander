# #словари и кортежи
#
#Домашняя работа №4
#
INAI = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
# del INAI['bag']
# INAI.update(address='Тимирязева74')
# #INAI['address'] ='Тимирязева74'
# INAI['phone'] = '044422211'
# INAI['insta'] = '@inai'
# courses = ['java']
# INAI['courses'].append('html css')
# INAI['courses'].extend(courses)
# for k, v in INAI.items():
#     print(f'{k}-{v}')
# print(INAI)

# #1 Удалить ключ bag
# #2 Адресс КГПИ изменить на нынешний
# #3 Добавить телефон КГПИ и Инстаграмм аккаунт
# #4 Расширить курсы актуальными
# #5 Преобразовать пары ключ и значение
#
#
#
# #словари
# #1-у словаря есть ключ и значение/ ключи должны уникальными/ и они любого типа данных
#
# # person = {
# #     'name': 'Ivan',
# #     'age': 49,
# #     'education': True,
# #     1997: False,
# #     145: True,
# #     'weight': 55.55,
# #     'nummer': ['0555111222', '0777111222']
# # }
# #
# # #добавление
# # person['cars'] = 'bmw'
# # #измение
# # person['age'] = 50
# # #удаление
# # del person[145]
# # person['nummer'].append('0999111222')
# # print(person.keys())
# # print(person.values())
# # print(person['nummer'][1])
# # print(person)
# #
# # for keys, values in person.items():
# #     print(f'{keys}-{values}')
# #
# #
# # money = (1,3,5,10,20,50,100,200,500,1000,2000,5000)
# # person = (False, False, False, False, 'Satylganov', 'Datka', 'Moldo', 'OSmonov', 'Karalaev',
# #           'Balasagyn', False, 'Chokmorov')
# #
# # nominal = dict(zip(money, person))
# # for i,j in nominal.items():
# #     print(f'{i}-{j}')
# # print(nominal)
#
#
#
#
#
#
# #кортежи  -  списки те же самые но не изменяются
# # data_types = ('hello', 123, 33.44)
# #чтобы изменить надо перезаписать его в список(list)
# # data_types = list(data_types)
# # data_types.append(222222)
# # data_types = tuple(data_types)
# # print(data_types)
