#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    first = input("Первое значение: ")
    second = input("Второе значение: ")

    first_num = float(first)
    second_num = float(second)

    result = first_num + second_num
    print(f"Результат: {result}")
except ValueError:
    result = first + second
    print(f"Результат: {result}")
