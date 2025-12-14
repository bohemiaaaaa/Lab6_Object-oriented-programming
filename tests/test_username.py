#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from task1 import UsernameAlreadyExistsError, existing_usernames
from task1 import main as username_main


def test_username_already_exists():
    """Тест исключения при существующем имени"""
    with pytest.raises(UsernameAlreadyExistsError) as exc_info:
        raise UsernameAlreadyExistsError("Егор")

    assert "Егор" in str(exc_info.value)
    assert "UsernameAlreadyExistsError" in str(exc_info.value)


def test_username_registration_success(monkeypatch, capsys):
    """Тест успешной регистрации"""
    original_length = len(existing_usernames)
    inputs = iter(["NewUser"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    username_main()
    captured = capsys.readouterr()

    assert "успешно зарегистрировано" in captured.out
    assert "NewUser" in existing_usernames
    assert len(existing_usernames) == original_length + 1


def test_username_registration_failure(monkeypatch, capsys):
    """Тест неудачной регистрации"""
    inputs = iter(["Егор"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    username_main()
    captured = capsys.readouterr()

    assert "UsernameAlreadyExistsError" in captured.out
    assert "Егор" in captured.out
