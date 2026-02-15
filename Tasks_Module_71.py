# Задача 1. Форматирование цены
def format_price_range(price_start: int | None = None, price_end: int | None = None) -> str:
    if price_start is None and price_end is None:
        return 'Цена не указана'
    def get_unit_value_price(price: int ) -> tuple[str, int | float]:
        if price >= 1_000_000_000:
            return ' млрд', round(price / 1_000_000_000, 1)
        elif price >= 1_000_000:
            return ' млн', round(price / 1_000_000, 1)
        elif price >= 1_000:
            return ' тыс', round(price / 1_000, 1)
        else:
            return '', price
    def format_value_price(value_price: int | float) -> int | float:
        if value_price.is_integer():
            return (int(value_price))
        else:
            return value_price
    if price_start is not None:
        unit_price_start, value_price_start = get_unit_value_price(price_start)
        value_price_start = format_value_price(value_price_start)
    if price_end is not None:
        unit_price_end, value_price_end = get_unit_value_price(price_end)
        value_price_end = format_value_price(value_price_end)
    if price_start and price_end:
        if unit_price_start == unit_price_end:
            return f'{value_price_start} - {value_price_end}{unit_price_start} ₽'
        else:
            return f'{value_price_start}{unit_price_start} - {value_price_end}{unit_price_end} ₽'
    elif price_start:
        return f'от {value_price_start}{unit_price_start} ₽'
    elif price_end:
        return f'до {value_price_end}{unit_price_end} ₽'