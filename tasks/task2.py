#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import List


def main() -> None:
    try:
        rows: int = int(input("Введите количество строк: "))
        cols: int = int(input("Введите количество столбцов: "))

        matrix: List[List[int]] = []
        for i in range(rows):
            row: List[int] = []
            for j in range(cols):
                row.append(random.randint(1, 100))
            matrix.append(row)

        print("Сгенерированная матрица:")
        for row in matrix:
            print(row)

    except ValueError:
        print("Ошибка: введите целые числа для строк и столбцов!")


if __name__ == "__main__":
    main()
