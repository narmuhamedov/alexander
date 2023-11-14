# #дед
# class IphoneX:
#     def __init__(self, size, camera, color, nfc, memory):
#         self.size = size
#         self.camera = camera
#         self.color = color
#         self.nfc = nfc
#         self.memory = memory
#
#     def fast_charging(self, watt):
#         return f'этот телефон поддерживает - {watt} зарядки'
#
#     def __str__(self):
#         return f'{self.size}\n{self.camera}\n{self.color}\n{self.nfc}\n{self.memory}GB'
#
# phone_object = IphoneX(size=str(input('Какой размер телефона?')),
#                        camera=int(input('Введите пиксили камер')), color='black', nfc=True, memory=128)
# print(phone_object)
# print(phone_object.fast_charging(str(input('Какая у вас зарядка'))))
#
# #отец
# class Iphone_11(IphoneX):
#     def __init__(self, size, camera, color, nfc, memory, ik_port):
#         super().__init__(size, camera, color, nfc, memory)
#         self.ik_port = ik_port
#
#     def smart_house(self, TV, WashMashine, Led):
#         return (f'{TV}\n'
#                 f'{WashMashine}\n'
#                 f'{Led}')
#
#     def __str__(self):
#         return super().__str__()+f'\n{self.ik_port}'
#
#
# phone_object2 = Iphone_11(size=str(input('Какой размер телефона?')),
#                        camera=int(input('Введите пиксили камер')), color='black',
#                           nfc=True, memory=128, ik_port=False)
#
# print('-'*20)
# print(phone_object2)
# print(phone_object2.fast_charging(120))
# print(phone_object2.smart_house(True, True, False))
#
# #Внук
# class Iphone13(Iphone_11):
#     def __init__(self, size, camera, color, nfc, memory, ik_port):
#         super().__init__(size, camera, color, nfc, memory, ik_port)
#
#     def __str__(self):
#         return super().__str__()
#
# phone_object3 = Iphone_11(size=str(input('Какой размер телефона?')),
#                        camera=int(input('Введите пиксили камер')), color='black',
#                           nfc=True, memory=128, ik_port=True)
#
# print('-'*20)
# print(phone_object3)
# print(phone_object3.fast_charging(120))
# print(phone_object3.smart_house(True, True, False))



class Car:
    def __init__(self, marka, volume, color):
        self.marka = marka
        self.volume = volume
        self.color = color

    def drive(self, right_left_helm):
        return right_left_helm

    def __str__(self):
        return f'{self.marka}\n{self.volume}\n{self.color}'


class FuelCar(Car):
    def __init__(self, marka, volume, color, fuel):
        super().__init__(marka, volume, color)
        self.fuel =fuel

    def __str__(self):
        return super().__str__()+f'\n{self.fuel}'


class ElectricCar(Car):
    def __init__(self, marka, volume, color):
        super().__init__(marka, volume, color)