from Tasks_Module_71 import format_price_range
import pytest

@pytest.mark.parametrize("price_start,price_end,price_range", [
    (None, None, 'Цена не указана'),
    (2_001, None, 'от 2 тыс ₽'),
    (None, 100_500, 'до 100.5 тыс ₽'),
    (None, 10_050_000, 'до 10.1 млн ₽'),
    (20, 30, '20 - 30 ₽'),
    (20, 300_000, '20 - 300 тыс ₽'),
    (2_001, 300_000, '2 - 300 тыс ₽'),
    (1_000, 2_000_000, '1 тыс - 2 млн ₽'),
])
def test_format_price_range(price_start, price_end, price_range):
    result = format_price_range(price_start, price_end)
    assert result == price_range