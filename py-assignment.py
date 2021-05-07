# PYTHON ASSIGNMENT

# num_of_courses variable declared to get courses input from user
num_of_courses = int(input("How many courses did you finish? : "))

# Empty array to store course marks
course_marks = []

# While loop for getting the user input (courses’ marks)
counter = 1
while counter <= num_of_courses:

    course_marks.append(
        float(input(f"Enter your marks for course {counter} : ")))
    counter += 1

# For loop for just printing the marks
for marks in course_marks:
    print(marks)

# For loop to find the total of the marks
Total = 0
for marks in course_marks:
    Total += marks

# average variable to calculate average of marks
average = Total/len(course_marks)

print(f"Your average for your {num_of_courses} courses is: {average}")

# Grades are assigned accordingly

if average >= 90 and average <= 100:
    print("Your grade is A+")
elif average >= 80 and average <= 89:
    print("Your grade is B")
elif average >= 70 and average <= 79:
    print("Your grade is C")
elif average >= 60 and average <= 69:
    print("Your grade is D")
else:
    print("Your grade is F")
