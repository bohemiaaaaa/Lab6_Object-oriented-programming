#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UsernameAlreadyExistsError(Exception):
    def __init__(self, username: str, message: str = "имя уже занято") -> None:
        self.username: str = username
        self.message: str = message
        super(UsernameAlreadyExistsError, self).__init__(message)

    def __str__(self) -> str:
        return f"UsernameAlreadyExistsError: '{self.username}' -> {self.message}"


# Список занятых имен
existing_usernames: list[str] = ["Егор", "админ", "администратор", "admin"]


def main() -> None:
    try:
        new_username: str = input("Введите новое имя пользователя: ")

        if new_username in existing_usernames:
            raise UsernameAlreadyExistsError(new_username)
        else:
            existing_usernames.append(new_username)
            print(f"Имя пользователя '{new_username}' успешно зарегистрировано!")

    except UsernameAlreadyExistsError as e:
        print(e)


if __name__ == "__main__":
    main()
