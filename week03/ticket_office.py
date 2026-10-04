tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    name = input("Customer name (or q to quit): ").strip()
    if name.lower() == "q":
        break

    age_input = input("Age: ").strip()
    age = int(age_input)
    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ["weekday", "weekend"]:
        print("Invalid day.")
        continue

    student = input("Student (yes/no): ").strip().lower()
    if student not in ["yes", "no"]:
        print("Please answer yes or no.")
        continue

    if day == "weekday":
        base_price = 200.0
    else:
        base_price = 250.0

    if age < 6:
        category = "Free"
        discount_rate = 1.00
    elif age >= 65:
        category = "Senior"
        discount_rate = 0.50
    elif 6 <= age <= 12:
        category = "Child"
        discount_rate = 0.40
    elif student == "yes" and age <= 25:
        category = "Student"
        discount_rate = 0.30
    else:
        category = "Standard"
        discount_rate = 0.00

    price = base_price * (1 - discount_rate)
    print(f"{name}: {price:.2f} TRY ({category})")

    tickets_sold += 1
    total_revenue += price
    if category == "Free":
        free_tickets += 1

if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
