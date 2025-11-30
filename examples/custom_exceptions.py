#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Пользовательское исключение
class NegValException(Exception):
    pass


try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException("Neg val: " + str(val))
    print(val + 10)
except NegValException as e:
    print(e)

# Генерация исключения
try:
    raise Exception("Some exception")
except Exception as e:
    print("Exception exception " + str(e))
