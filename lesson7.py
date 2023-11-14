print('Здравствуйте возьмите стаканчик')
cash = int(input('Внесите наличку! '))
print(f'Баланс - {cash}')

while cash != 0:
    print('-'*20)
    coffe = str(input('Выберите кофе\n'
                       '1-Латте\n'
                       '2-Американо\n'
                       '3-Капучино\n'
                       '4-АйсКофе\n'))
    print('-' * 20)
    if coffe == '1':
        print('-' * 20)
        print('Латте стоит 20р')
        print('-' * 20)
        answer = str(input('Вы уверенны в своем заказе?да/нет '))
        if answer == "да":
            cash -= 20
            print(f'У вас осталось денег на карте : {cash}\n'
                  f'Вы купили Кофе №{coffe}\n'
                  f'1-Латте\n'
                       '2-Американо\n'
                       '3-Капучино\n'
                       '4-АйсКофе\n')
            break
        elif answer == 'нет':
            button_exit = int(input('Нажмите кнопку 1 для выхода'))
            if button_exit == 1:
                print('Всего хорошего')
                break
            else:
                print('Пожалуйста нажмите 1')
                continue

    elif coffe == '2':
        print('-' * 20)
        print('Американо стоит 50р')
        print('-' * 20)
        answer = str(input('Вы уверенны в своем заказе?да/нет '))
        if answer == "да":
            cash -= 50
            print(f'У вас осталось денег на карте : {cash}\n'
                  f'Вы купили Кофе №{coffe}\n'
                  f'1-Латте\n'
                       '2-Американо\n'
                       '3-Капучино\n'
                       '4-АйсКофе\n')
            break
        elif answer == 'нет':
            button_exit = int(input('Нажмите кнопку 1 для выхода'))
            if button_exit == 1:
                print('Всего хорошего')
                break
            else:
                print('Пожалуйста нажмите 1')
                continue

    elif coffe == '3':
        print('-' * 20)
        print('Капучино стоит 60р')
        print('-' * 20)
        answer = str(input('Вы уверенны в своем заказе?да/нет '))
        if answer == "да":
            cash -= 60
            print(f'У вас осталось денег на карте : {cash}\n'
                  f'Вы купили Кофе №{coffe}\n'
                  f'1-Латте\n'
                       '2-Американо\n'
                       '3-Капучино\n'
                       '4-АйсКофе\n')
            break
        elif answer == 'нет':
            button_exit = int(input('Нажмите кнопку 1 для выхода'))
            if button_exit == 1:
                print('Всего хорошего')
                break
            else:
                print('Пожалуйста нажмите 1')
                continue


    elif coffe == '4':
        print('-' * 20)
        print('Латте стоит 20р')
        print('-' * 20)
        answer = str(input('Вы уверенны в своем заказе?да/нет '))
        if answer == "да":
            cash -= 90
            print(f'У вас осталось денег на карте : {cash}\n'
                  f'Вы купили Кофе №{coffe}\n'
                  f'1-Латте\n'
                       '2-Американо\n'
                       '3-Капучино\n'
                       '4-АйсКофе\n')
            break
        elif answer == 'нет':
            button_exit = int(input('Нажмите кнопку 1 для выхода'))
            if button_exit == 1:
                print('Всего хорошего')
                break
            else:
                print('Пожалуйста нажмите 1')
                continue
