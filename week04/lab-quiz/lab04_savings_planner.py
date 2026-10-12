def main():
    while True:
        starting_balance = float(input("Enter starting balance: "))
        if starting_balance >= 0:
            break
        print("Starting balance cannot be negative. Try again.")

    while True:
        monthly_deposit = float(input("Enter monthly deposit: "))
        if monthly_deposit > 0:
            break
        print("Monthly deposit must be positive. Try again.")

    while True:
        interest_rate = float(input("Enter monthly interest rate (%): "))
        if interest_rate >= 0:
            break
        print("Interest rate cannot be negative. Try again.")

    while True:
        savings_goal = float(input("Enter savings goal: "))
        if savings_goal > 0:
            break
        print("Savings goal must be positive. Try again.")

    if starting_balance >= savings_goal:
        print(f"\nGoal already reached with starting balance of {starting_balance:.2f}!")
        print(f"Final balance: {starting_balance:.2f}")
        print("Total interest earned: 0.00")
        return

    current_balance = starting_balance
    total_interest = 0.0
    month = 0
    goal_reached = False

    print("\nMonth | Interest Earned | New Balance")
    print("-" * 37)

    while month < 60:
        month += 1
        interest = current_balance * (interest_rate / 100)
        current_balance += interest + monthly_deposit
        total_interest += interest

        print(f"{month:<5} | {interest:<15.2f} | {current_balance:<11.2f}")

        if current_balance >= savings_goal:
            goal_reached = True
            break

    print("-" * 37)
    if goal_reached:
        print(f"Goal reached in {month} month(s)!")
    else:
        print("Goal not reached after 60 months.")

    print(f"Final balance: {current_balance:.2f}")
    print(f"Total interest earned: {total_interest:.2f}")


if __name__ == "__main__":
    main()
