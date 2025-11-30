#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile

import pytest
from exceptions import DataFormatError, InvalidPhoneError
from models import Contact, PhoneBook
from storage import load_phonebook, save_phonebook


def test_contact_creation():
    """Тест создания контакта"""
    contact = Contact("Иванов", "Иван", "79101234567", "01.01.1990")
    assert contact.last_name == "Иванов"
    assert contact.first_name == "Иван"
    assert contact.phone == "79101234567"
    assert contact.birth_date == "01.01.1990"


def test_phonebook_add_valid():
    """Тест добавления корректного контакта"""
    phonebook = PhoneBook()
    phonebook.add("Петров", "Петр", "79051234567", "15.05.1985")

    assert len(phonebook.contacts) == 1
    assert phonebook.contacts[0].last_name == "Петров"
    assert phonebook.contacts[0].phone == "79051234567"


def test_phonebook_add_invalid_phone():
    """Тест добавления контакта с некорректным телефоном"""
    phonebook = PhoneBook()

    with pytest.raises(InvalidPhoneError):
        phonebook.add("Сидоров", "Алексей", "abc", "20.10.1990")


def test_phonebook_add_short_phone():
    """Тест добавления контакта с коротким телефоном"""
    phonebook = PhoneBook()

    with pytest.raises(InvalidPhoneError):
        phonebook.add("Сидоров", "Алексей", "123", "20.10.1990")


def test_phonebook_select():
    """Тест поиска по фамилии"""
    phonebook = PhoneBook()
    phonebook.add("Иванов", "Иван", "79101234567", "01.01.1990")
    phonebook.add("Петров", "Петр", "79051234567", "15.05.1985")
    phonebook.add("Иванов", "Мария", "79211234567", "10.10.1995")

    result = phonebook.select("Иванов")
    assert len(result) == 2
    assert all(contact.last_name == "Иванов" for contact in result)


def test_phonebook_sorting():
    """Тест сортировки по первым трем цифрам телефона"""
    phonebook = PhoneBook()
    phonebook.add("Иванов", "Иван", "79211234567", "01.01.1990")  # 792
    phonebook.add("Петров", "Петр", "79051234567", "15.05.1985")  # 790
    phonebook.add("Сидоров", "Алексей", "79101234567", "20.10.1990")  # 791

    # Должны быть отсортированы: 790, 791, 792
    assert phonebook.contacts[0].phone == "79051234567"
    assert phonebook.contacts[1].phone == "79101234567"
    assert phonebook.contacts[2].phone == "79211234567"


def test_save_and_load_phonebook():
    """Тест сохранения и загрузки телефонной книги"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
        temp_filename = f.name

    try:
        phonebook = PhoneBook()
        phonebook.add("Иванов", "Иван", "79101234567", "01.01.1990")
        phonebook.add("Петров", "Петр", "79051234567", "15.05.1985")

        save_phonebook(phonebook, temp_filename)

        loaded_phonebook = load_phonebook(temp_filename)

        assert len(loaded_phonebook.contacts) == 2

        assert loaded_phonebook.contacts[0].last_name == "Петров"
        assert loaded_phonebook.contacts[0].phone == "79051234567"
        assert loaded_phonebook.contacts[1].last_name == "Иванов"
        assert loaded_phonebook.contacts[1].phone == "79101234567"

    finally:
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_load_invalid_xml():
    """Тест загрузки некорректного XML"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
        f.write("Это не XML файл")
        temp_filename = f.name

    try:
        with pytest.raises(DataFormatError):
            load_phonebook(temp_filename)
    finally:
        if os.path.exists(temp_filename):
            os.unlink(temp_filename)


def test_phonebook_str_empty():
    """Тест строкового представления пустой телефонной книги"""
    phonebook = PhoneBook()
    result = str(phonebook)
    assert "Телефонный справочник пуст" in result


def test_phonebook_str_with_contacts():
    """Тест строкового представления с контактами"""
    phonebook = PhoneBook()
    phonebook.add("Иванов", "Иван", "79101234567", "01.01.1990")
    result = str(phonebook)

    assert "Иванов" in result
    assert "Иван" in result
    assert "79101234567" in result
    assert "01.01.1990" in result
