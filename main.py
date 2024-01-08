# Creating variables for user input
Name = input("Enter Your Name: ")

# Initialize lists to store Homework grades
Homework_1_grades = []
Homework_2_grades = []

while True:
    Homework_1 = -1
    while Homework_1 < 0 or Homework_1 > 10:
        try:
            Homework_1 = float(input("Enter Homework 1 Grade: "))  # Convert input to float
        except:
            if Homework_1 == complex or str:
                print("an error has occured, please use a numerical value")
            else:
                if Homework_1 == int:
                    print("No Errors Have Been Detected")
    Homework_1_grades.append(Homework_1)  # Add the grade to the list
    alt_grade = input("Would you like to enter an alternative Homework 1 grade? (Y/N): ")
    if alt_grade.lower() != 'y':
        break  # If the user enters anything other than 'Y', exit the loop

while True:
    Homework_2 = -1
    while Homework_2 < 0 or Homework_2 > 10:
        try:
            Homework_2 = float(input("Enter Homework 2 Grade: "))  # Convert input to float
        except:
            if Homework_2 == complex or str:
                print("an error has occured, please use a numerical value")
            else:
                if Homework_2 == int:
                    print("No Errors Have Been Detected")
    Homework_2_grades.append(Homework_2)  # Add the grade to the list
    alt_grade = input("Would you like to enter an alternative Homework 2 grade? (Y/N): ")
    if alt_grade.lower() != 'y':
        break  # If the user enters anything other than 'Y', exit the loop

Midterm_exam = -1 
while Midterm_exam < 0 or Midterm_exam > 100:
    try:
        Midterm_exam = float(input("Enter Midterm Score: "))
    except:
        if Midterm_exam == complex or str:
            print("an error has occured, please use a numerical value")
        else:
            if Midterm_exam == int:
                print("No Errors Have Been Detected")
    if Midterm_exam < 70:
        print("Better Luck Next Time")

Final_exam = -1 
while Final_exam < 0 or Final_exam > 100:
    try:
        Final_exam = float(input("Enter Final Score: "))
    except:
        if Final_exam == complex or str:
            print("an error has occured, please use a numerical value")
        else:
            if Final_exam == int:
                print("No Errors have been detected")
    if Final_exam < 70:
        print("Better Luck Next Time")


# Calculate the overall grade for Homework
Overall_Homework = ((sum(Homework_1_grades) + sum(Homework_2_grades)) / (len(Homework_1_grades) + len(Homework_2_grades))) * 30

# Assign letter grades to individual components
def get_letter_grade(score):
    if score >= 93:
        return 'A'
    elif score == 90-90.2:
        return 'A-'
    elif score == 87-89.9:
        return 'B+'
    elif score == 83-86.9:
        return 'B'
    elif score == 80-82.9:
        return 'B-'
    elif score == 77-79.9:
        return 'C+'
    elif score == 73-76.9:
        return 'C'
    elif score == 70-72.9:
        return 'C-'
    elif score == 67-69.9:
        return 'D+'
    elif score == 63-66.9:
        return 'D-'
    elif score == 60-62.9:
        return 'D'
    else:
        return 'F'

# Assign letter grades to each component
Homework_1_letter_grade = get_letter_grade(Homework_1)
Homework_2_letter_grade = get_letter_grade(Homework_2)
Overall_Homework_letter_grade = get_letter_grade(Overall_Homework)
Midterm_exam_letter_grade = get_letter_grade(Midterm_exam)
Final_exam_letter_grade = get_letter_grade(Final_exam)

# Calculate the total grade
Final_test_grade = ((Midterm_exam + Final_exam) / 200) * 70
Overall_Class_Grade = Overall_Homework + Final_test_grade

# Assign letter grade to overall class grade
Overall_Class_Grade_letter_grade = get_letter_grade(Overall_Class_Grade)

#Create a file to write name and final letter grade to said file
f = open("info.txt", "w")
f.write("Student Name: " + Name + "Final Letter Grade: " + Overall_Class_Grade_letter_grade)
f.close()

# Printing out results with letter grades
print("Name:", Name)
print("Homework 1 Grade:", Homework_1, "Letter Grade:", Homework_1_letter_grade)
print("Homework 2 Grade:", Homework_2, "Letter Grade:", Homework_2_letter_grade)
print("Overall Homework Grade:", Overall_Homework, "Letter Grade:", Overall_Homework_letter_grade)
print("Midterm Exam Grade:", Midterm_exam, "Letter Grade:", Midterm_exam_letter_grade)
print("Final Exam Grade:", Final_exam, "Letter Grade:", Final_exam_letter_grade)
print("Total Class Grade (Unrounded):", Overall_Class_Grade, "Letter Grade:", Overall_Class_Grade_letter_grade)

# Opening and displaying contents of the text file
f = open("info.txt", "r")
print("The contents of the file info.txt include the following: ", f.read())
    
# Flowchart
#   Start
#   |
#   Input Name
#   |
#   Input Homework 1 Grade
#   Input Homework 2 Grade
#   Input Midterm Exam Grade
#   Input Final Exam Grade
#   |
#   Check for positive and negative grades
#   |
#   Calculate the total grade
#   Calculate the rounded decimal grade
#   Calculate letter grade
#   |
#   Print Name, Total Grade, Rounded Total Grade, and Letter Grade
#   |
#   End
