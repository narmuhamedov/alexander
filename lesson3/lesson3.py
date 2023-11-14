









#Структура данных списки и кортежи

#Списков - Объекты находящиеся в одной переменной разного типа данных

# name = 'Alexander'
# name = list(name)
# name.insert(4, 4)
# print(name)



#номера элементов 0   1     2     3      4        5
#data_list = ['hello', 123, True, False, 'world', 12.44]
# #Списки - добавлять
# data_list.append('Alexander')#append добавляет новый элемент в конец списка
# data_list.append('Far Cry 5')
#2 - добавляет элемент между индексами
# data_list.insert(2, "Radomir")
# data_list.insert(1, 'Android')

#Удаление
# data_list.remove(False)
# del data_list[2]

#Изменение
#data_list[1]=1997

#print(data_list)

###2 Сортировка и реверсация
# number = [1,3,2,4,6,5,8,7,0]
# number.sort()
# print(number)
#
# name = ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r']
# name.reverse()
# print(name)

#перемещение элемента с одного списка в другой
# men = ['Ivan', 'Dima', 'Anton']
# women = ['Masha', 'Vera', 'Lubov']
# women.insert(1, men.pop(1))
# #women.append(men.pop(1))
# print(men)
# print(women)


ded = [12, True, 'R', 'A', 'D', 'o', 11, 12.33]
sestra = list()
jena = list()
brat = list()
for vnuk in ded:
    if type(vnuk) == str:
        jena.append(vnuk)
    elif type(vnuk)==int:
        sestra.append(vnuk)
    else:
        brat.append(vnuk)

brat.remove(12.33)
sestra.sort()
jena[1]='a'
jena[2]='d'

print(sestra)
print(brat)
print(jena)






# name = 'Alex'
# age = 30
# print(f'Имя-{name}\n'
#       f'Возраст-{age}')