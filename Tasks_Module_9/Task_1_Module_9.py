# Задание 1
# Описание работы:
# 1. Программа запрашивает у пользователя текст.
# 2. Каждая новая фраза должна записываться в файл notes.txt с новой строки, не удаляя старые данные.
# 3. Перед каждой фразой автоматически добавляется текущая дата и время (модуль datetime).
# 4. Цикл завершается, когда пользователь вводит слово "стоп".
from datetime import datetime
with open('notes.txt', mode= 'a') as notes_text:
    while True:
        datetime_note = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        text = input('Введите вашу заметку: ')
        if text.lower() == 'стоп':
            break
        notes_text.write(f'{datetime_note}\n')
        notes_text.write(f'{text}\n')