#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Contact:
    last_name: str
    first_name: str
    phone: str
    birth_date: str


@dataclass
class PhoneBook:
    contacts: List[Contact] = field(default_factory=list)

    def add(self, last_name: str, first_name: str, phone: str, birth_date: str) -> None:
        from exceptions import InvalidPhoneError

        if not phone.isdigit() or len(phone) != 11:
            raise InvalidPhoneError(phone)

        self.contacts.append(
            Contact(
                last_name=last_name,
                first_name=first_name,
                phone=phone,
                birth_date=birth_date,
            )
        )

        self.contacts.sort(key=lambda contact: contact.phone[:3])

    def select(self, last_name: str) -> List[Contact]:
        result: List[Contact] = [
            contact
            for contact in self.contacts
            if contact.last_name.lower() == last_name.lower()
        ]
        return result

    def __str__(self) -> str:
        if not self.contacts:
            return "Телефонный справочник пуст"

        table: List[str] = []
        line: str = "+{}-+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 20, "-" * 15, "-" * 15, "-" * 12
        )
        table.append(line)
        table.append(
            "| {:^4} | {:^20} | {:^15} | {:^15} | {:^12} |".format(
                "№", "Фамилия", "Имя", "Телефон", "Дата рождения"
            )
        )
        table.append(line)

        for idx, contact in enumerate(self.contacts, 1):
            table.append(
                "| {:>4} | {:<20} | {:<15} | {:<15} | {:<12} |".format(
                    idx,
                    contact.last_name,
                    contact.first_name,
                    contact.phone,
                    contact.birth_date,
                )
            )
        table.append(line)

        return "\n".join(table)
