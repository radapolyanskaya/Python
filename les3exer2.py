# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:57:36 2021

@author: Anna Streltsova
"""
#Реализовать функцию, принимающую несколько параметров, описывающих 
#данные пользователя: имя, фамилия, год рождения, город проживания, 
#email, телефон. Функция должна принимать параметры как именованные 
#аргументы. Реализовать вывод данных о пользователе одной строкой.

def person_info(name, surname, year_of_birth, city, email, telephone):
    result = f' Данные о пользователе: {name},{surname},{year_of_birth},{city},{email},{telephone}'
    return result
print(person_info('Anna', 'Streltsova', 1991, 'Moscow', 'radapolyanskaya@mail.ru', 89265299135))


