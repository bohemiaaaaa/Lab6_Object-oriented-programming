#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Базовый пример обработки исключений
print("start")
try:
    val = int(input("input number: "))
    tmp = 10 / val
    print(tmp)
except Exception as e:
    print("Error! " + str(e))
print("stop")

# Обработка конкретных исключений
print("start")
try:
    val = int(input("input number: "))
    tmp = 10 / val
    print(tmp)
except ValueError as ve:
    print("ValueError! {0}".format(ve))
except ZeroDivisionError as zde:
    print("ZeroDivisionError! {0}".format(zde))
except Exception as ex:
    print("Error! {0}".format(ex))
print("stop")

# Блок finally
try:
    val = int(input("input number: "))
    tmp = 10 / val
    print(tmp)
except Exception:  # Исправлено: было bare 'except'
    print("Exception")
finally:
    print("Finally code")

# Блок else
try:
    f = open("tmp.txt", "r")
    for line in f:
        print(line)
    f.close()
except Exception as e:
    print(e)
else:
    print("File was readed")
