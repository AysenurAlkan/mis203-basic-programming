total_students = 0
total_score = 0

while True:
    name = input("Enter student name (or q to quit): ")
    if name == "q":
        break

    score = int(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    # Harf notunu belirleyeceğim.
    if score >= 90 and score <= 100:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "F"

    # Her öğrenci için ekrana yazdırıp sayacı arttıracağım.
    print(f"{name}: {score} -> {grade}")
    total_students += 1
    total_score += score

# Döngü bittikten sonra çalışacak
if total_students == 0:
    print("No students entered.")
else:
    average_score = total_score / total_students
    print(f"Total students: {total_students}")
    print(f"Average score: {average_score:.2f}")
