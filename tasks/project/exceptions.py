#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InvalidPhoneError(Exception):
    def __init__(
        self, phone: str, message: str = "Некорректный номер телефона"
    ) -> None:
        self.phone = phone
        self.message = message
        super().__init__(f"{phone} -> {message}")


class UnknownCommandError(Exception):
    def __init__(self, command: str, message: str = "Неизвестная команда") -> None:
        self.command = command
        self.message = message
        super().__init__(f"{command} -> {message}")


class DataFormatError(Exception):
    def __init__(
        self, filename: str, message: str = "Некорректная структура файла"
    ) -> None:
        self.filename = filename
        self.message = message
        super().__init__(f"{filename} -> {message}")
