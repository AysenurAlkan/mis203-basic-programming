def calculate_subtotal(unit_price: float, quantity: int) -> float:
    return unit_price * quantity


def get_discount_rate(subtotal: float) -> float:
    if subtotal >= 100.0:
        return 0.10
    return 0.00


def calculate_shipping_fee(subtotal: float) -> float:
    if subtotal >= 50.0:
        return 0.0
    return 15.0


def calculate_final_total(unit_price: float, quantity: int) -> float:
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_rate = get_discount_rate(subtotal)
    discount_amount = subtotal * discount_rate
    shipping_fee = calculate_shipping_fee(subtotal)
    
    return (subtotal - discount_amount) + shipping_fee


assert calculate_subtotal(20.0, 3) == 60.0
assert get_discount_rate(100.0) == 0.10
assert get_discount_rate(99.99) == 0.00
assert calculate_shipping_fee(60.0) == 0.0
assert calculate_final_total(20.0, 3) == 60.0


def print_quote(order_name: str, unit_price: float, quantity: int):
    subtotal = calculate_subtotal(unit_price, quantity)
    discount = get_discount_rate(subtotal) * 100
    shipping = calculate_shipping_fee(subtotal)
    total = calculate_final_total(unit_price, quantity)
    
    print(f"--- {order_name} ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount Rate: {discount:.0f}%")
    print(f"Shipping Fee: ${shipping:.2f}")
    print(f"Final Total: ${total:.2f}\n")


if __name__ == "__main__":
    print_quote("Order 1 (Standard)", unit_price=20.0, quantity=3)
    print_quote("Order 2 (Above Threshold)", unit_price=30.0, quantity=4)
