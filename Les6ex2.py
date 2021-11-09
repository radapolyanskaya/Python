# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:39:34 2021

@author: Anna Streltsova
"""
#Реализовать класс Road (дорога), в котором определить атрибуты: 
#length (длина), width (ширина). Значения данных атрибутов должны 
#передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: 
#длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить 
#работу метода.
class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(20000, 6)
road_to_village.intake()