#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os

from exceptions import DataFormatError, InvalidPhoneError, UnknownCommandError
from models import PhoneBook
from storage import load_phonebook, save_phonebook

os.makedirs("tasks/project", exist_ok=True)

logging.basicConfig(
    filename="tasks/project/program.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s:%(message)s",
)


def main() -> None:
    phonebook: PhoneBook = PhoneBook()

    try:
        phonebook = load_phonebook("tasks/project/data.xml")
        print("Данные загружены автоматически")
        logging.info("Данные загружены автоматически при запуске")
    except (DataFormatError, FileNotFoundError):
        print("Файл данных не найден или поврежден, начинаем с пустой базы")
        logging.info("Начало работы с пустой базой данных")

    print("Телефонный справочник")
    print("Введите 'help' для просмотра команд")

    while True:
        try:
            command: str = input(">>> ").lower().strip()

            if command == "exit":
                print("Завершение работы...")
                break

            elif command == "add":
                last_name: str = input("Фамилия: ")
                first_name: str = input("Имя: ")
                phone: str = input("Номер телефона (11 цифр): ")
                birth_date: str = input("Дата рождения (дд.мм.гггг): ")

                phonebook.add(last_name, first_name, phone, birth_date)
                print("Контакт успешно добавлен")
                log_msg = f"Добавлен: {last_name} {first_name}"
                logging.info(log_msg)

            elif command == "list":
                print(phonebook)
                logging.info("Отображен список контактов")

            elif command.startswith("select"):
                parts: list[str] = command.split(" ", maxsplit=1)
                if len(parts) > 1:
                    last_name: str = parts[1]
                    selected = phonebook.select(last_name)

                    if selected:
                        msg = f"Найдено с фамилией '{last_name}': {len(selected)}"
                        print(msg)
                        for idx, contact in enumerate(selected, 1):
                            contact_info = (
                                f"{idx}: {contact.first_name} "
                                f"{contact.last_name}, тел: {contact.phone}, "
                                f"рожд: {contact.birth_date}"
                            )
                            print(contact_info)
                        log_msg = f"Найдено {len(selected)} контактов"
                        logging.info(log_msg)
                    else:
                        msg = f"Контакты с фамилией '{last_name}' не найдены"
                        print(msg)
                        logging.warning(msg)
                else:
                    error_msg = "Ошибка: используйте 'select <фамилия>'"
                    print(error_msg)
                    logging.error(error_msg)

            elif command.startswith("save "):
                parts: list[str] = command.split(" ", maxsplit=1)
                if len(parts) > 1:
                    filename: str = "tasks/project/" + parts[1]
                    save_phonebook(phonebook, filename)
                    print(f"Данные сохранены в файл: {filename}")
                    logging.info(f"Данные сохранены в файл: {filename}")
                else:
                    error_msg = "Ошибка: используйте 'save <имя_файла>'"
                    print(error_msg)
                    logging.error(error_msg)

            elif command.startswith("load "):
                parts: list[str] = command.split(" ", maxsplit=1)
                if len(parts) > 1:
                    filename: str = "tasks/project/" + parts[1]
                    phonebook = load_phonebook(filename)
                    print(f"Данные загружены из файла: {filename}")
                    logging.info(f"Данные загружены из файла: {filename}")
                else:
                    error_msg = "Ошибка: используйте 'load <имя_файла>'"
                    print(error_msg)
                    logging.error(error_msg)

            elif command == "help":
                print("Список команд:")
                print("add - добавить контакт")
                print("list - показать все контакты")
                print("select <фамилия> - найти по фамилии")
                print("save <файл> - сохранить в XML")
                print("load <файл> - загрузить из XML")
                print("help - показать справку")
                print("exit - выйти")

            else:
                raise UnknownCommandError(command)

        except InvalidPhoneError as e:
            error_msg = f"InvalidPhoneError: {e}"
            print(f"Ошибка: {e}")
            logging.error(error_msg)
        except UnknownCommandError as e:
            error_msg = f"UnknownCommandError: {e}"
            print(f"Ошибка: {e}")
            logging.error(error_msg)
        except DataFormatError as e:
            error_msg = f"DataFormatError: {e}"
            print(f"Ошибка формата данных: {e}")
            logging.error(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            print(f"Неизвестная ошибка: {e}")
            logging.error(error_msg)


if __name__ == "__main__":
    main()
