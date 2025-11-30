#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task1 import main as addition_main


def test_addition_numbers(monkeypatch, capsys):
    """Тест сложения чисел"""
    inputs = iter(["5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    addition_main()
    captured = capsys.readouterr()
    assert "Результат: 8.0" in captured.out


def test_addition_strings(monkeypatch, capsys):
    """Тест конкатенации строк"""
    inputs = iter(["hello", "world"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    addition_main()
    captured = capsys.readouterr()
    assert "Результат: helloworld" in captured.out


def test_addition_mixed(monkeypatch, capsys):
    """Тест смешанных типов"""
    inputs = iter(["5", "world"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    addition_main()
    captured = capsys.readouterr()
    assert "Результат: 5world" in captured.out
