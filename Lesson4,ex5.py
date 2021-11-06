# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:49:22 2021

@author: Anna Streltsova
"""
#Реализовать формирование списка, используя функцию range() и возможности
# генератора. В список должны войти четные числа от 100 до 1000 
#(включая границы). Необходимо получить результат вычисления произведения
# всех элементов списка.
#Подсказка: использовать функцию reduce().

from functools import reduce
new_list = [i for i in range(100,1000) if i % 2 == 0]
summa = reduce((lambda x, y: x * y), new_list)
print(summa)