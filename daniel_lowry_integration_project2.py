# Name: Daniel J. Lowry
# Description: Modified version of the sprint 1 quiz.


## 1: Simple I/O - print() function with end= and sep= arguments ##

print("\n\nHello user", end='!\n', )
print("Welcome to SATMATHNOW - Practice Exam 1", end='!\n', )
print("This program is designed to help you prepare for the SAT Math portion of the test", sep=',', end='!\n\n')

# Input Function

name_for_input = input("\n\n\nPlease type your name here so that we can record your visit: ")
print("Welcome " + name_for_input + "!" + " And thank you for using SATMATHNOW!", end='\n\n')

# Exam Instructions

print("A few instructions before beginning the practice exam: ", end='\n\n\n')
print("1. You are allowed to use a calculator for the entire exam.", end='\n')
print("2. This practice exam is NOT multiple choice, please type a specific answer to each question.", end='\n')
print("3. Unlike the real SAT, this practice exam does not have a time limit, but we encourage you to pace yourself.",
      end='\n\n\n')


# Exam Start Confirmation

def start_exam_confirm():
    exam_confirm = input("Type 'y' to confirm you want to start the exam. Press 'n' to close the exam. ")
    while (exam_confirm != 'y' and exam_confirm != 'n'):
        print("Error: Invalid input. Please input 'y' or 'n' only.\n")
        exam_confirm = input("Type 'y' to confirm you want to start the quiz. Press 'n' to close the exam. ")
    if (exam_confirm == 'n'):
        quit()


start_exam_confirm()

## Basic calculations ##

# Exponent (**)

exponent1 = int(input("\n\n1. What is does 5 raised to the power of 4 equal(5^4)? "))

if (exponent1 == 5 ** 4):
    print("\nCorrect!")
else:
    print("\nIncorrect, remember 5^4 is 5x5x5x5.")

exponent2 = int(input("\n\n2. Solve 11^6. "))

if (exponent2 == 11 ** 6):
    print("\nCorrect!")
if (exponent2 > 11 ** 6):
    print("\nIncorrect, your answer is too high.")
if (exponent2 < 11 ** 6):
    print("\nIncorrect, your answer is too low.")

# Multiplication (*)

multiply1 = int(input("\n\n3. What is the product of 11 and 12? "))

if (multiply1 == 11 * 12):
    print("\nCorrect!")
else:
    print("\nIncorrect, remember 'product' refers to multiplication")

multiply2 = int(input("\n\n4. Solve 26 x 5. "))

if (multiply2 == 26 * 5):
    print("\nCorrect!")

if (multiply2 != 26 * 5):
    print("\nIncorrect, check your calculations.")

# Division (/)

divide1 = int(input("\n\n5. What is the quotient of 96 and -12? "))

if (divide1 == 96 / -12):
    print("\nCorrect!")
else:
    print("\nIncorrect, 'quotient' refers to division. So in this case, 96 is divided by -12.")

# Modulo (//)

modulo1 = int(input("\n\n6. What is the remainder of the quotient of 75 and 8? "))

if (modulo1 == 75 // 8):
    print("\nCorrect!")
else:
    print("\nIncorrect,divide 75 by 8. Whatever number remains is the answer.\n")

# String Multiplcation (*)

print("Sandwich, " * 12, end=" ")
str_oper_multi_1 = int(input("\n\n7. How many words can be seen here? "))

if (str_oper_multi_1 == 12):
    print("\nCorrect!\n\n")
else:
    print("\nIncorrect.\n\n")

# String Addition (+)

print("barnacle,", "barnacle, ", "barnacle, ", "barnacle, ", "barnacle, ", "barnacle, ", "barnacle, ", end=" ")
str_oper_add_1 = int(input("\n\n8. How many words are present above? "))

if (str_oper_add_1 == 7):
    print("\nCorrect!")
else:
    print("\nIncorrect.")



# End of Exam & Review Score

def review_score_response():
    print("\n\n\nYou have now reached the end of the exam. Thank you for choosing SATMATHNOW.")
    review_score = int(input("Please rate the quality of the practice exam from 1 to 10. "))

    if (review_score <= 5 and review_score >= 1):
        print(
            "\nIn order to improve our exams in the future, please write a short explanation as to why you rate the exam " + str(
                review_score) + " out of 10.\n")
        input()
        print("\n\nThank you for your feedback, and have a good day!\n")
    elif (review_score >= 6 and review_score <= 10):
        print("\nThank you for your feedback, and have a good day!\n")
    else:
        print("\nInvalid input. Please only type a number from 1 to 10.\n")


review_score_response()

# Additional Sprint 2 Requirements that don't fit the quiz theme

print("If you are seeing this message, then the requirements for the 'sprint 2' were not met in the quiz above.")
print("This is because the requirements for the assignment were unable to fit into the theme of an SAT practice exam.")
print("As such, any remaining requirements will be placed here. These do not have any central theme or focus.")
print("They merely serve to complete every requirement for the assignment.")

# For + Range + In requirement

for_range_in_input = input("\n\n1. Please enter your favorite color: ")
for color in range(10):
    print(for_range_in_input)

# Boolean Operators - not, or

not_or_input = int(input("\n\n2. Please enter a number from 1 to 100. "))
print(not(not_or_input <= 0 or not_or_input >= 101))

# Shortcut Operators

shortcut_operator1 =  int(input("\n\n3. Please enter a number from  1 to 50. "))
comparing_number1 = 0

while (comparing_number1 <= shortcut_operator1):
    print(comparing_number1)
    comparing_number1 += 1

shortcut_operator2 = int(input("\n\n4. Please enter another number 1 to 50. "))
comparing_number2 = 100

while(comparing_number2 >= shortcut_operator2):
    print(comparing_number2)
    comparing_number2 -= 1

# Parameter Passing Function

def printGreaterNumber(num1, num2):
    if (num2 > num1):
        greater_number = num2
    else:
        greater_number = num1
    return greater_number

def printGreaterNumberCall():
    num_input1 = int(input("\n\n5. Please enter a number. "))
    num_input2 = int(input("\n6. Please enter another number. "))

    greater_number = printGreaterNumber(num_input1, num_input2)
    print("The larger number between your two inputs is ", greater_number)

printGreaterNumberCall()

# Cited Sources:

# 1. GeeksforGeeks. (2022, July 20). Python end parameter in print(). GeeksforGeeks.
# Retrieved September 18, 2022, from https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

# 2. GeeksforGeeks. (2021, January 21). Python: Sep Parameter in print(). GeeksforGeeks.
# Retrieved September 18, 2022, from https://www.geeksforgeeks.org/python-sep-parameter-print/


# Submission Instructions:
# 1. Submit .py file as before and...
# 2. Create a GitHub repository for your program, upload your Main.py file through the browser, and submit a link to it
# as a submission comment.
