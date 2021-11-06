# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:53:20 2021

@author: Anna Streltsova
"""
#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного
# заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools. 
#Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
#Необходимо предусмотреть условие его завершения.
from itertools import cycle, count

v_start = int(input('Start number: '))
v_stop = v_start * 2 + 10 + 1

# v.1
for i in count(v_start):
    if i < v_stop:
        print(i)
    else:3
        break
del i

# v.2
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break