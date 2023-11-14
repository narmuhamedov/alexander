#условные операторы if elif else
#циклы while

#Условные операторы
#TODO if - работает на условии если мы уверенны на 100% данного действия
#TODO elif - работает тогда когда есть 2ой вариант действия (50 на 50)
#TODO else - работает тогда когда нету больше никаких вариантов


#while - цикл бесконечности
# while 1:
#     print('Привет Алекс')


#пример сортировка яблок на хорошие и плохие
#!-не

apple_box = 10
good_box = 0
bad_box = 0

while apple_box !=0:
    question = str(input('Какое яблоко? 1-хорошее 0-плохое '))
    if question == '1':
        apple_box -=1
        good_box +=1
        print(f'общее кол-во яблок:{apple_box}\n'
              f'хороших:{good_box}\n'
              f'плохих:{bad_box}')

    elif question == '0':
        apple_box-=1
        bad_box+=1
        print(f'общее кол-во яблок:{apple_box}\n'
              f'хороших:{good_box}\n'
              f'плохих:{bad_box}')

print('--------------------------------')
print(f'Плохие{bad_box}\n'
      f'Хорошие{good_box}')








#пример сфетофор lower -нижний регистр upper - верний регистр
# while 1:
#     color = str(input('Какой сейчас горит цвет? ').lower())
#     if color == 'red':
#         print(f'сейчас горит {color} STOP!')
#
#     elif color == 'yellow':
#         print(f'сейчас горит {color} READY or STOP!')
#
#     elif color == 'green':
#         print(f'сейчас горит {color} GO!')
#
#     else:
#         print("Смотреть по ситуации!!!")
#
#     exit = str(input('Вы хотите завершить игру? да/нет '))
#     if exit == 'да':
#         print('Спасибо за игру Досвидания!')
#         break
#     elif exit == 'нет':
#         print('Супер давайте продолжим')
#         continue

