#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

from exceptions import DataFormatError
from models import Contact, PhoneBook


def save_phonebook(phonebook: PhoneBook, filename: str) -> None:
    root = ET.Element("phonebook")

    for contact in phonebook.contacts:
        contact_element = ET.Element("contact")

        last_name_element = ET.SubElement(contact_element, "last_name")
        last_name_element.text = contact.last_name

        first_name_element = ET.SubElement(contact_element, "first_name")
        first_name_element.text = contact.first_name

        phone_element = ET.SubElement(contact_element, "phone")
        phone_element.text = contact.phone

        birth_date_element = ET.SubElement(contact_element, "birth_date")
        birth_date_element.text = contact.birth_date

        root.append(contact_element)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as fout:
        tree.write(fout, encoding="utf-8", xml_declaration=True)


def load_phonebook(filename: str) -> PhoneBook:
    try:
        with open(filename, "r", encoding="utf8") as fin:
            xml = fin.read()

        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)

        phonebook = PhoneBook()

        for contact_element in tree:
            last_name: str = ""
            first_name: str = ""
            phone: str = ""
            birth_date: str = ""

            for element in contact_element:
                if element.tag == "last_name":
                    last_name = element.text or ""
                elif element.tag == "first_name":
                    first_name = element.text or ""
                elif element.tag == "phone":
                    phone = element.text or ""
                elif element.tag == "birth_date":
                    birth_date = element.text or ""

            if all([last_name, first_name, phone, birth_date]):
                phonebook.contacts.append(
                    Contact(
                        last_name=last_name,
                        first_name=first_name,
                        phone=phone,
                        birth_date=birth_date,
                    )
                )

        phonebook.contacts.sort(key=lambda contact: contact.phone[:3])
        return phonebook

    except Exception as e:
        raise DataFormatError(filename) from e
