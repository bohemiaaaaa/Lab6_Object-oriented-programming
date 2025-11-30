#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

# Базовое логирование
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug message!")
logging.info("Info message!")
logging.warning("Warning message!")
logging.error("Error message!")
logging.critical("Critical message!")

# Логирование исключений
logging.basicConfig(filename="log.txt", level=logging.INFO)
try:
    print(10 / 0)
except Exception as e:
    logging.error(str(e))
