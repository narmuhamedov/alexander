import random
from random import randint, sample
import datetime
print('Добро пожаловать в казино')
start = datetime.datetime.now()
try:
    cash = int(input('Внесите вашу ставку '))
    print(f'Вы внесли - {cash}')
    if cash <= 0:
        print('Не пытайтесь меня обмануть вводите нормальные деньги!')
except:
    print('Произошла ошбика системы!')

# cash = 1000
while cash != 0:
        try:
            bet = int(input(f'Какую сумму из {cash} желаете поставить! '))
            if bet>cash:
                print('У вас не хватает денег!')
                continue
            person = [randint(1, 6), randint(1,6)]
            computer = [randint(1, 6), randint(1,6)]
        except:
            print('Вводите только число')
            continue

        if sum(person) > sum(computer):
            cash += bet
            print(f'Вы выйграли у вас денег {cash}')
        elif sum(person) < sum(computer):
            cash -= bet
            print(f'Вы проиграли у вас денег {cash}')
        else:
            print('Ничья!!!')


endgame = datetime.datetime.now() - start
print(f'Вы провели в игре - {endgame}')








#
# lst = ['apple', 'banana', 'orange', 'peach', 'strawberry']
# print(sample(lst, 2))
# print(randint(100, 300))