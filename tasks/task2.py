#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

try:
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 100))
        matrix.append(row)

    print("Сгенерированная матрица:")
    for row in matrix:
        print(row)

except ValueError:
    print("Ошибка: введите целые числа для строк и столбцов!")
