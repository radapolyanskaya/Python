# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:14:57 2021

@author: Anna Streltsova
"""

#Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента. 
#Использовать функцию type() для проверки типа. Элементы списка
 #можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [10, None, -43, 'True', True, 9.5]
def my_type(el):
 for el in range(len(my_list)):
        print(type(my_list[el]))
 return
my_type(my_list)
