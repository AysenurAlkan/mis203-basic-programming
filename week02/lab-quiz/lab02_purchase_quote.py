item_one = input("First item: ").strip()
quantity_one = int(input("First quantity: "))
price_one = float(input("First unit price: "))
item_two = input("Second item:" ).strip()
quantity_two = int(input("Second quantity: "))
price_two = float(input("Second unit price: "))
shipping = float(input("Shipping charge: "))
tax_percent = float(input(" Tax percentage (0-100): "))

line_one = quantity_one * price_one
line_two = quantity_two * price_two
subtotal = line_one + line_two
tax = subtotal * tax_percent / 100
final_total = subtotal + tax + shipping

print()
print(f" {item_one } {quantity_one } x {price_one: .2f} = {line_one: .2f}")
print(f" {item_two } {quantity_two } x {price_two: .2f} = {line_two: .2f}")
print(f" Subtotal: {subtotal: .2f} TRY")
print(f" Tax ({tax_percent: .1f}%): {tax: .2f} TRY")
print(f" Shipping:  {shipping: .2f} TRY")
print(f" TOTAL:  {final_total: .2f} TRY")

