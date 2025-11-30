#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from task2 import main as matrix_main


def test_matrix_creation(monkeypatch, capsys):
    """Тест создания матрицы"""
    inputs = iter(["2", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    matrix_main()
    captured = capsys.readouterr()

    assert "Сгенерированная матрица:" in captured.out
    # Проверяем что выведено 2 строки матрицы
    lines = [line for line in captured.out.split("\n") if line.strip().startswith("[")]
    assert len(lines) == 2


def test_matrix_invalid_input(monkeypatch, capsys):
    """Тест неверного ввода"""
    inputs = iter(["abc", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    matrix_main()
    captured = capsys.readouterr()

    assert "Ошибка: введите целые числа для строк и столбцов!" in captured.out
