from Tasks_Module_71 import format_price_range
import pytest

@pytest.mark.parametrize("price_start,price_end,price_range", [
    (None, None, 'Цена не указана'),
    (1000, 2000, '1 - 2 тыс. ₽'),
    (1000, 2000000, '1 тыс. - 2 млн. ₽'),
    (1000, None, 'от 1 тыс. ₽'),
    (None, 20000, 'до 20 тыс. ₽'),
])
def test_format_price_range(price_start, price_end, price_range):
    result = format_price_range(price_start, price_end)
    assert result == price_range