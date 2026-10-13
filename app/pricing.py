SHIPPING_RATE = 0.05
MAX_QUANTITY = 10


def summarize(lines, is_prime):
    """Totals for (unit_price, quantity) pairs. Prime members ship free."""
    subtotal = round(sum(price * quantity for price, quantity in lines), 2)
    shipping = 0.0 if is_prime else round(subtotal * SHIPPING_RATE, 2)
    return {
        'count': sum(quantity for _, quantity in lines),
        'subtotal': subtotal,
        'shipping': shipping,
        'shipping_saved': round(subtotal * SHIPPING_RATE, 2) if is_prime else 0.0,
        'total': round(subtotal + shipping, 2),
    }
