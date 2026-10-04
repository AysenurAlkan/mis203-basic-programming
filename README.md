# mis203-basic-programming
- **Name:** Ayşenur Alkan
- **Student Number:** 2404109054
- **Department:** Management Information Systems
- **Course Name:** MIS 203 Basic Programming

### AI Usage Note ~week01
- **AI Tool Used:** Gemini
- **Prompt Used:** "Write a simple Python program that asks the user for their name, department, age, and career goal, then prints a short student profile with header '--- Student Profile ---'.
- **What did you change? :** I updated the print statements to use clean f-string and added input prompts so that the console output matches the assignment format exactly.
  
### AI Usage Note ~week02
- **AI Tool Used:** Gemini
- **Prompt Used:** "I shared my draft code and the assignment requirements to ask where my indentation and logic errors were, and how to fix the grade calculation loop."
- **What did you change?** I fixed the indentation errors inside the while loop so the student counters would update properly. I also corrected the grade conditions and moved the summary statistics outside the loop.
- **What does break do in your program?** "It helps me exit the while loop whenever I am done adding students and type 'q'."

## AI Usage Note ~week03
- **AI Tool Used:** Gemini
- **Prompt Used:** "Write a cinema ticket program with while loop, input validation, and discount rules."
- **What did you change?** I added `.strip()` to clean inputs and fixed summary print formatting.
- **Tests:**
  1. Age 5, Weekend, Student no -> `0.00 TRY (Free)` (boundary: under 6)
  2. Age 12, Weekday, Student yes -> `120.00 TRY (Child)` (boundary: age 12, child before student)
  3. Age 26, Weekday, Student yes -> `200.00 TRY (Standard)` (boundary: age 26, student limit)
- **Why does the order of the rules matter?** Python evaluates from top to bottom. If student was first, a 10-year-old child would wrongly get the lower student discount instead of the child discount.
