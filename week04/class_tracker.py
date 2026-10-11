print("=== CLASS ARRIVAL TRACKER ===")

total_students = 0

while True:
    student_name = input("\nStudent Name (or q to quit): ")
    if student_name.lower() == 'q':
        break
    
    time_left = int(input("Time left before class (minutes): "))
    if time_left <= 0 or time_left > 180:
        print("Invalid time! Must be between 1 and 180 minutes.")
        continue

    walk_time = int(input("Walking time to bus stop (minutes): "))
    if walk_time < 0 or walk_time > 60:
        print("Invalid walking time!")
        continue

    bus_time = int(input("Bus travel time (minutes): "))
    if bus_time < 0 or bus_time > 60:
        print("Invalid bus time!")
        continue
      
    metro_time = int(input("Metro travel time (minutes): "))
    if metro_time < 0 or metro_time > 60:
        print("Invalid metro time!")
        continue

    tram_time = int(input("Tram travel time (minutes): "))
    if tram_time < 0 or tram_time > 60:
        print("Invalid tram time!")
        continue

    total_needed_time = walk_time + bus_time + metro_time + tram_time

    if total_needed_time > time_left:
        status = "YOU'RE LATE! Even if the bus flies you won't make it. Might as well stay in bed."
    elif total_needed_time == time_left:
        status = "ON THE EDGE! If you run, you'll slide into class right as the lecture starts."
    else:
        status = "YOU'LL MAKE IT! You even have enough time to grab a coffee before class."

    total_students += 1
    print(f"\n{student_name.capitalize()} - Total travel time: {total_needed_time} mins | Time left: {time_left} mins")
    print(f"Result: {status}")

print("\n" + "="*35)
if total_students > 0:
    print(f"Total students analyzed: {total_students}")
else:
    print("No students analyzed.")
