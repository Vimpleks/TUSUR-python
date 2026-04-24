import pytest
from Tasks_Module_101 import safe_divide, parse_date, InvalidDateFormatError


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_zero_value_error():
    with pytest.raises(ValueError) as ex:
        safe_divide(10, 0)
    assert ex.value.args[0] == "Деление на ноль"

def test_safe_divide_value_not_int_type_error():
    with pytest.raises(TypeError) as ex:
        safe_divide('10', 2)
    assert ex.value.args[0] == "Аргументы должны быть числами"


def test_parse_date():
    assert parse_date("25.12.2024") == (25, 12, 2024)

def test_parse_date_not_str():
    with pytest.raises(InvalidDateFormatError) as ex:
        parse_date(25)
    assert ex.value.args[0] == "Входные данные должны быть строкой"

def test_parse_date_incorrect_format():
    with pytest.raises(InvalidDateFormatError) as ex:
        parse_date("2024-12-25")
    assert ex.value.args[0] == "Дата должна быть в разделена '.'"

def test_parse_date_incorrect_type():
    with pytest.raises(InvalidDateFormatError) as ex:
        parse_date("ab.cd.efgh")
    assert ex.value.args[0] == "День, месяц и год должны быть числами"