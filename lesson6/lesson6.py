# #lambda fuction и исключения try  except
# summa = lambda a, b: a+b
# print(summa(1, 4))
#
# words = ['apple', 'banana', 'strawberry', 'orange']
# len_w = list(filter(lambda x: len(x)>5, words))
# print(len_w)
#
# list_= ['word', 'python', 'java']
# big = list(map(lambda x: x.upper(), list_))
# print(big)

#try except

while 1:
    try:
        number = int(input('Введите первое число '))
        operation = str(input('+ - / * '))
        number2 = int(input('Введите второе число '))
    except:
        print('Пожалуйста пишите только цифры')
        continue

    if operation == '+':
        print(number+number2)
    elif operation == '-':
        print(number-number2)

    elif operation == '*':
        print(number * number2)

    elif operation == '/':
        try:
            print(number/number2)
        except:
            print('На ноль делить нельзя! ')
            continue

# try:
#     number = 1
#     number2 = 2
#     print(number+number2)
# except:
#     print('Складывать число со строкой нельзя')
#
#



# def average(*args):
#     return sum(args)/len(args)
#
#
# print(average(12, 33, 444, 555, 440))
#
#


# def my_family(role, name, age=18):
#     return (f'{role}-{name}-{age}\n')
#
# print(my_family(role='Отец', name='Иван', age=50))
# print(my_family(role='Мать', name='Мария', age=45))
# print(my_family(role='Сын', name='Борис', age=25))
# print(my_family(role='Дочь', name='Алина', age=20))
