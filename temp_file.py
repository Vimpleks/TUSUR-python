def get_unit_price(price: int) -> tuple[str, int | float]:
    if price >= 1_000_000_000:
        return 'млрд.', round(price / 1_000_000_000, 1)
    elif price >= 1_000_000:
        return 'млн.', round(price / 1_000_000, 1)
    elif price >= 1_000:
        return 'тыс.', round(price / 1_000, 1)
    else:
        return '', price

print(get_unit_price(5050))
print(type(round(5.050, 1)))
print(5.0.is_integer())