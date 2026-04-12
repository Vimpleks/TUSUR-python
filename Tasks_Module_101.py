import tracemalloc
from contextlib import contextmanager

# Упражнение 1: Безопасное деление
def safe_divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Деление на ноль")
    except TypeError:
        raise TypeError("Аргументы должны быть числами")

# Упражнение 2: Парсинг даты
class InvalidDateFormatError(Exception):
    pass

def parse_date(date_string: str) -> tuple | None:
    if not isinstance(date_string, str):
        raise InvalidDateFormatError("Входные данные должны быть строкой")
    date_list = date_string.split(".")
    if len(date_list) != 3:
        raise InvalidDateFormatError("Дата должна быть в разделена '.'")
    try:
        date_list_digits = map(int, date_list)
        return tuple(date_list_digits)
    except ValueError:
        raise InvalidDateFormatError("День, месяц и год должны быть числами")

# Упражнение 3: Контекстный менеджер для измерения памяти
@contextmanager
def memory_usage():
    tracemalloc.start()
    start_memory, peak = tracemalloc.get_traced_memory()
    try:
        yield
    finally:
        end_memory, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory_difference = (end_memory - start_memory) / (1024 * 1024)
        print(f"Использовано памяти: {memory_difference:.2f} MB")

with memory_usage():
    data = [i ** 2 for i in range(1_000_000)]