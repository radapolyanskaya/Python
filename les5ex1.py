# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:53:51 2021

@author: Anna Streltsova
"""
 #Создать программно файл в текстовом формате, записать в него построчно
# данные, вводимые пользователем. Об окончании ввода данных свидетельствует
# пустая строка
my_list = []
while True:
    line = input("Введите что-нибудь: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("test_1.txt", "w") as file_obj:
        file_obj.writelines(my_list)