# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:58:00 2021

@author: Anna Streltsova
"""
#Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево). А также методы: go,
# stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов:
#TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. 
#Для классов TownCar и WorkCar переопределите метод show_speed. При 
#значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться 
#сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов и 
#также покажите результат.
class Car:

    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
            # if (not self.speed or len(self.speed) <= 0) or \
            #         (not self.color or len(self.color) <= 0) or \
            #         (not self.name or len(self.name) <= 0) or \
            #         not bool(self.is_police):
            #     raise BaseException
        except BaseException:
            return "Error. Please, enter data."
            exit(-1)

    def go(self):
        return "Go."

    def stop(self):
        return "Stop."

    def turn_left(self):
        return "Turn left."

    def turn_right(self):
        return "Turn right."

    def show_speed(self):
        print("Machine normal speed.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


toyota = SportCar(100, 'Red', 'Toyota', False)
mazda = TownCar(30, 'White', 'Mazda', True)
suzuki = WorkCar(70, 'Rose', 'Suzuki', False)
honda = PoliceCar(110, 'Blue',  'honda', True)


print(toyota.turn_left())
print(mazda.turn_right())
print(suzuki.stop())
print(honda.go())
print(suzuki.is_police)
print(honda.is_police)
print(suzuki.show_speed())
print(honda.show_speed())