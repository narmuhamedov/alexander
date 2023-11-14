# class Sport:
#     def __init__(self, judo, sambo, wressling, football, basketball, ice_hockey):
#         self.judo = judo
#         self.sambo = sambo
#         self.wrestling = wressling
#         self.football = football
#         self.basketball = basketball
#         self.ice_hockey = ice_hockey
#
#     def answer_sport(self, answer):
#         if answer == 'judo':
#             print(f'{answer} - одежда кимоно и место проведения татами')
#         elif answer == 'sambo':
#             print(f'{answer} - одежда самбовка и место проведения ковер')
#         elif answer == 'wrestling':
#             print(f'{answer} - одежда трико и место проведения ковер')
#         elif answer == 'football':
#             print(f'{answer} - одежда шорты и футболка и место проведения поле')
#         elif answer == 'basketball':
#             print(f'{answer} - одежда шорты и футболка и место проведения спортзал')
#         elif answer == 'ice_hockey':
#             print(f'{answer} - одежда хоккейная экипировка и место проведения лед')
#
#     def __str__(self):
#         return (f'{self.judo}\n'
#                 f'{self.sambo}\n'
#                 f'{self.wrestling}\n'
#                 f'{self.football}\n'
#                 f'{self.basketball}\n'
#                 f'{self.ice_hockey}')
#
# all_sport = Sport(judo='Дзюдо', sambo='Самбо', wressling='Борьба', football='Футбол',
#                   basketball='Баскетбалл', ice_hockey='Хоккей')
# print(all_sport)
# print(all_sport.answer_sport(str(input('Напишите название спорта!'))))

#
# class Usuall_Laptop:
#     def __init__(self, name, year, color, cpu):
#         self.name = name
#         self.year = year
#         self.color = color
#         self.cpu = cpu
#
#     def can_play_games(self, chance):
#         if self.cpu <= 2:
#             return f'У {self.name} для игры шанс равен = {chance} = 0% '
#         elif  2 <= self.cpu <= 8:
#             return f'У {self.name} для игры шанс равен = {chance} = 50%'
#         else:
#             return f'У {self.name} для игры шанс равен = {chance} = 100%'
#
#     def __str__(self):
#         return (f'Имя{self.name}\n'
#                 f'Год{self.year}\n'
#                 f'Цвет{self.color}\n'
#                 f'Память{self.cpu}GB')
#
# pentium1 = Usuall_Laptop(name='Lenovo', year=1997, color='black', cpu=4)
# print(pentium1.can_play_games(''))
# print(pentium1)
#
#
# class GameLaptop(Usuall_Laptop):
#     def __init__(self, name, year, color, cpu, volume_battery):
#         super().__init__(name, year, color, cpu)
#         self.volume_battery = volume_battery
#
#     def __str__(self):
#         return super(GameLaptop, self).__str__()+f'\nБатарея{self.volume_battery}'
#
# print('-'*20)
# game_laptop1 = GameLaptop(name='Acer', year=2023, color='black', cpu=120,
#                           volume_battery=5000)
# print(game_laptop1.can_play_games(''))
# print(game_laptop1)
#
# class GameAndWorkLaptop(GameLaptop):
#     def __init__(self, name, year, color, cpu, volume_battery, cooler):
#         super().__init__(name, year, color, cpu, volume_battery)
#         self.cooler = cooler
#
#     def __str__(self):
#         return super().__str__()+f'\nКол-во вентов - {self.cooler}'
#


class Judo:
    def wresling(self, arena):
        return arena

class Sambo:
    def wresling(self, arena):
        return arena

class Sumo:
    def wresling(self, arena):
        return arena

person_1 = Judo()
person_2 = Sambo()
person_3 = Sumo()

print(person_1.wresling('Татами'))
print(person_2.wresling('Ковер'))
print(person_3.wresling('Ковер для сумоистов'))



