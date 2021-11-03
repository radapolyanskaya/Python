# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:17:21 2021

@author: Anna Streltsova
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn
"""
n = input("Enter number: ")
a = int(n + n)
b = int(n+n+n)
summa = int(n) + a + b

print(summa) 
