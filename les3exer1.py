# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:21:51 2021

@author: Anna Streltsova
"""
# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.
def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "Нельзя делить на нуль"
    except ValueError:
        return "введите число"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
