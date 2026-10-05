order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
member_input = (
    input("Is the customer a member? (yes/no): ").strip().lower())

is_member = member_input in ["yes", "y"]

if requested_quantity <= 0:
    print("\n[REJECTED] Invalid quantity (must be greater than 0).")

elif requested_quantity >= available_stock:
    print(f"\n[REJECTED] Insufficient stock! Available: {available_stock}, Requested: {requested_quantity}")

else:
    approval_reason = "Sufficient stock available and valid quantity requested."
    print(f"\n[APPROVED] Reason: {approval_reason}")

    if is_member and order_amount >= 500:
        discount = order_amount * 0.10
        final_price = order_amount - discount
        print("A 10% member discount has been applied.")
    else:
        final_price = order_amount
        if is_member:
            print("No discount applied: Order amount is below 500 TRY threshold.")
        else:
            print("No discount applied: Customer is not a member.")

    print(f"Final Price: {final_price:.2f} TRY")
