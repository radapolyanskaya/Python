# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:45:57 2021

@author: Anna Streltsova
"""
#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора 
#класса (метод __init__()), который должен принимать данные 
#(список списков) для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин, 
#расположенных в виде прямоугольной схемы.
#Примеры матриц вы найдете в методичке.
#Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции 
#сложения двух объектов класса Matrix (двух матриц). Результатом 
#сложения должна быть новая матрица.
class Matrix:

    template_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __init__(self, matrix_list_1, matrix_list_2):
        self.matrix_list_1 = matrix_list_1
        self.matrix_list_2 = matrix_list_2

    def __str__(self):
        return str(
            '\n'.join([
                str('\t'.join([
                    str(self.template_matrix[a][b]) for b in range(len(self.template_matrix[a]))
                ])) for a in range(len(self.template_matrix))
            ])
        )

    def __add__(self):
        for a in range(len(self.matrix_list_1)):
            for b in range(len(self.matrix_list_2[a])):
                self.template_matrix[a][b] = self.matrix_list_1[a][b] + self.matrix_list_2[a][b]
        return self.__str__()


print(Matrix([[5, 18, 11], [6, 17, 23], [41, 30, 9]], [[5, 18, 11], [6, 17, 23], [41, 50, 9]]).__add__())