# Задание 3
# Создайте логгер, который:
# 1. Выводит все сообщения с отметкой времени, уровнем, названием функции и номером строки исходного кода, откуда был вызван логгер.
# 2. Направляет все сообщения уровня ERROR и выше в файл err.log.
# 3. Направляет все сообщения уровней INFO и WARNING в файл app.log.
# 4. Направляет все сообщения уровня DEBUG размером не больше 50 символов в консоль.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
"{asctime} : {levelname} : {funcName} : {lineno} : {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

def info_warning_filter(record: logging.LogRecord) -> bool:
    return record.levelname == 'INFO' or record.levelname == 'WARNING'

def debug_filter(record: logging.LogRecord) -> bool:
    return record.levelname == 'DEBUG' and len(record.msg) <= 50

err_file_handler = logging.FileHandler('err.log')
err_file_handler.setFormatter(formatter)
err_file_handler.setLevel(logging.ERROR)

info_warning_handler = logging.FileHandler('app.log')
info_warning_handler.setFormatter(formatter)
info_warning_handler.addFilter(info_warning_filter)

debug_console_handler = logging.StreamHandler()
debug_console_handler.setFormatter(formatter)
debug_console_handler.addFilter(debug_filter)

logger.addHandler(err_file_handler)
logger.addHandler(info_warning_handler)
logger.addHandler(debug_console_handler)