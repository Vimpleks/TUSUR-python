# Задание 4
# Представьте, что ваше приложение работает постоянно и генерирует много данных в логах. Для упрощения обработки логов
# такого приложения создайте логгер, который:
# 1. Записывает логи в файл до тех пор, пока размер файла не превысит 1Мб.
# 2. При достижении 1Мб выполняет смену файла и продолжает вести лог в новый файл.
# 3. Сохраняет последние 5 файлов размером 1 Мб (т.е. при заполнении 5  файла, логгер перезаписывает 1 сохраненный
#     и далее цикл сохранения файлов продолжается: file1 -> file2 -> file3 -> file4 -> file5 -> file1 -> file2 -> ...).

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
"{asctime} : {name} : {levelname} : {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

rotating_file_handler = RotatingFileHandler('task4_info.log', maxBytes=1048576, backupCount=5)
rotating_file_handler.setFormatter(formatter)

logger.addHandler(rotating_file_handler)

