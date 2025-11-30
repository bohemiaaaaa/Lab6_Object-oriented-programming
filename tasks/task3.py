#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UsernameAlreadyExistsError(Exception):
    def __init__(self, username, message="имя уже занято"):
        self.username = username
        self.message = message
        super(UsernameAlreadyExistsError, self).__init__(message)

    def __str__(self):
        return f"UsernameAlreadyExistsError: '{self.username}' -> {self.message}"


# Список занятых имен
existing_usernames = ["Егор", "админ", "администратор", "admin"]

try:
    new_username = input("Введите новое имя пользователя: ")

    if new_username in existing_usernames:
        raise UsernameAlreadyExistsError(new_username)
    else:
        existing_usernames.append(new_username)
        print(f"Имя пользователя '{new_username}' успешно зарегистрировано!")

except UsernameAlreadyExistsError as e:
    print(e)
