# Author: Daniel J. Lowry
# Description: SAT math practice exam.


# 1: Simple I/O - print() function with end= and sep= arguments #

print("\n\nHello user", end='!\n', )
print("Welcome to SATMATHNOW - Practice Exam 1", end='!\n', )
print("This program is designed to help you prepare for the SAT Math portion "
      "of the test", sep=',', end='!\n\n')
'''A short introduction to the program.'''

# Input Function

name_for_input = input("\n\n\nPlease type your name here so that we can "
                       "record your visit: ")
'''Prompts the user for name to record'''
print("Welcome " + name_for_input + "! " + "And thank you for using "
                                           "SATMATHNOW!", end='\n\n')
'''A welcome message using the name stored in the variable above this line'''

# Exam Instructions

print("A few instructions before beginning the practice exam: ", end='\n\n\n')
print("1. You are allowed to use a calculator for the entire exam.", end='\n')
print("2. This practice exam is NOT multiple choice, please type a specific "
      "answer to each question.", end='\n')
print("3. Unlike the real SAT, this practice exam does not have a time "
      "limit, but we encourage you to pace yourself.",
      end='\n\n\n')
'''Small instructions for the user before starting the exam.'''


# Exam Start Confirmation

def start_exam_confirm():
    exam_confirm = input("Type 'y' to confirm you want to start the exam. "
                         "Press 'n' to close the exam. ")
    '''Prompts the user for either a lowercase y or n to confirm they want to
       begin the exam'''
    while exam_confirm != 'y' and exam_confirm != 'n':
        print("Error: Invalid input. Please input 'y' or 'n' only.\n")
        exam_confirm = input("Type 'y' to confirm you want to start the "
                             "quiz. Press 'n' to close the exam. ")
        '''While loop for when the user does not enter one of the acceptable
           inputs'''
    if exam_confirm == 'n':
        quit()
        '''Exits the program if a lowercase n is entered'''


start_exam_confirm()

# Basic calculations #

# Exponent (**)

try:
    exponent1 = int(input("\n\n1. What is does 5 raised to the power of 4 "
                          "equal (5^4)? "))
except ValueError:
    print("\nPlease only input numerical values.")
    exponent1 = int(input("\n\n1. What is does 5 raised to the power of 4 "
                          "equal (5^4)? "))

if exponent1 == 5 ** 4:
    print("\nCorrect!")
else:
    print("\nIncorrect, remember 5^4 is 5x5x5x5.")
'''Prompts the user for the answer to the question 5^4, which is 625. Any other
input results in an "Incorrect" message displaying.'''

try:
    exponent2 = int(input("\n\n2. Solve 11^6. "))
except ValueError:
    print("\nPlease only input numerical values.")
    exponent2 = int(input("\n\n2. Solve 11^6. "))

if exponent2 == 11 ** 6:
    print("\nCorrect!")
if exponent2 > 11 ** 6:
    print("\nIncorrect, your answer is too high.")
if exponent2 < 11 ** 6:
    print("\nIncorrect, your answer is too low.")
'''Prompts the user for the answer to the question 11^6, which is 1,771,561.
Any other input results in an "Incorrect" message displaying, the incorrect
message varying depending on the user's answer.'''

# Multiplication (*)

try:
    multiply1 = int(input("\n\n3. What is the product of 11 and 12? "))
except ValueError:
    print("\nPlease only input numerical values.")
    multiply1 = int(input("\n\n3. What is the product of 11 and 12? "))

if multiply1 == 11 * 12:
    print("\nCorrect!")
else:
    print("\nIncorrect, remember 'product' refers to multiplication")
'''Prompts the user for the answer to the question 11 x 12, which is 132. Any
other input results in an "Incorrect" message displaying.'''

try:
    multiply2 = int(input("\n\n4. Solve 26 x 5. "))

except ValueError:
    print("\nPlease only input numerical values.")
    multiply2 = int(input("\n\n4. Solve 26 x 5. "))

if multiply2 == 26 * 5:
    print("\nCorrect!")
if multiply2 != 26 * 5:
    print("\nIncorrect, check your calculations.")
'''Prompts the user for the answer to the question 26 x 5, which is 130. Any
other input results in an "Incorrect" message displaying.'''

# Division (/)

try:
    divide1 = int(input("\n\n5. What is the quotient of 96 and -12? "))
except ValueError:
    print("\nPlease only input numerical values.")
    divide1 = int(input("\n\n5. What is the quotient of 96 and -12? "))

if divide1 == 96 / -12:
    print("\nCorrect!")
else:
    print("\nIncorrect, 'quotient' refers to division. So in this case, "
          "96 is divided by -12.")
'''Prompts the user for the answer to the question 96/-12, which is -8. Any
other input results in an "Incorrect" message displaying.'''

# Modulo (//)

try:
    modulo1 = int(input("\n\n6. What is the remainder of the quotient of 75 "
                        "and 8? "))
except ValueError:
    print("\nPlease only input numerical values.")
    modulo1 = int(
        input("\n\n6. What is the remainder of the quotient of 75 and "
              "8? "))

if modulo1 == 75 // 8:
    print("\nCorrect!")
else:
    print("\nIncorrect,divide 75 by 8. Whatever number remains is the "
          "answer.\n")
'''Prompts the user for the reminder of 75/8, which is 3. Any other
input results in an "Incorrect" message displaying.'''

# String Multiplication (*)

try:
    print("Sandwich, " * 12, end=" ")
    str_oper_multi_1 = int(input("\n\n7. How many words can be seen here? "))
except ValueError:
    print("\nPlease only input numerical values.")
    print("Sandwich, " * 12, end=" ")
    str_oper_multi_1 = int(
        input("\n\n7. How many words can be seen here? "))
'''Prints the word "sandwich" twelve times and asks the user to input the
number of times the word is displayed.'''

if str_oper_multi_1 == 12:
    print("\nCorrect!\n\n")
else:
    print("\nIncorrect.\n\n")
'''Prompts the user for the number of times the word is displayed, the answer
being 12. Any other input results in an "Incorrect" message displaying.'''

# String Addition (+)

try:
    print("barnacle,", "barnacle, ", "barnacle, ", "barnacle, ", "barnacle, ",
          "barnacle, ", "barnacle, ", end=" ")
    str_oper_add_1 = int(input("\n\n8. How many words are present above? "))
except ValueError:
    print("\nPlease only input numerical values.")
    print("barnacle,", "barnacle, ", "barnacle, ", "barnacle, ",
          "barnacle, ",
          "barnacle, ", "barnacle, ", end=" ")
    str_oper_add_1 = int(
        input("\n\n8. How many words are present above? "))
'''Similar to the previous question, prints out the word "barnacle" seven times
and asks the user for how many times the word is displayed.'''

if str_oper_add_1 == 7:
    print("\nCorrect!")
else:
    print("\nIncorrect.")
'''Prompts the user for the answer to the question above, which is 7. Any other
input results in an "Incorrect" message displaying.'''


# End of Exam & Review Score

def review_score_response():
    print("\n\n\nYou have now reached the end of the exam. Thank you for "
          "choosing SATMATHNOW.")
    review_score = int(input("Please rate the quality of the practice exam "
                             "from 1 to 10. "))
    '''Prompts the user for a review of the exam, from a scale of one to
    ten.'''
    if review_score <= 5:
        if review_score >= 1:
            print(
                "\nIn order to improve our exams in the future, please write "
                "a short explanation as to why you rate "
                "the exam " + str(
                    review_score) + " out of 10.\n")
            input()
            print("\n\nThank you for your feedback, and have a good day!\n")
            '''If the user inputs a number between one and five, inclusive, the
            program will ask the user to write to elaborate why they gave this
            review'''
    elif 6 <= review_score <= 10:
        print("\nThank you for your feedback, and have a good day!\n")
        '''If the user inputs a number between six and ten, inclusive, then a
        short thank you message displays.'''
    else:
        print("\nInvalid input. Please only type a number from 1 to 10.\n")
        '''Any other input displays an error message, and asks the user to
        reenter an acceptable input.'''


review_score_response()

# Additional Sprint 2 Requirements

# The code below refers to additional requirements of the "Sprint 2" assignment
# that did not fit the theme of the project, that being an SAT math exam.

print("If you are seeing this message, then the requirements for the 'sprint "
      "2' were not met in the quiz above.")
print("This is because the requirements for the assignment were unable to "
      "fit into the theme of an SAT practice exam.")
print("As such, any remaining requirements will be placed here. These do not "
      "have any central theme or focus.")
print("They merely serve to complete every requirement for the assignment.")
'''A short explanation telling the user about this additional section.'''

# For + Range + In requirement

for_range_in_input = input("\n\n1. Please enter your favorite color: ")
for color in range(10):
    print(for_range_in_input)
'''Prompts the user for an input, then displays said input ten times.'''

# Boolean Operators - not, or

try:
    not_or_input = int(input("\n\n2. Please enter a number from 1 to 100. "))
    print(not (not_or_input <= 0 or not_or_input >= 101))
except ValueError:
    print("\nPlease only input numerical values.")
    not_or_input = int(
        input("\n\n2. Please enter a number from 1 to 100. "))
    print(not (not_or_input <= 0 or not_or_input >= 101))
'''Prompts the user for a number between one and one hundred, will print "True"
if the number is from one to one hundred, inclusive. Will print "False" if not
within this boundary.'''

# Shortcut Operators

try:
    shortcut_operator1 = int(input("\n\n3. Please enter a number from  1 to "
                                   "50. "))
    comparing_number1 = 0
except ValueError:
    print("\nPlease only input numerical values.")
    shortcut_operator1 = int(
        input("\n\n3. Please enter a number from  1 to "
              "50. "))
    comparing_number1 = 0
'''Prompts the user for a number between one and fifty. As well as setting the
number it will be compared to zero.'''

while comparing_number1 <= shortcut_operator1:
    print(comparing_number1)
    comparing_number1 += 1
'''Constantly prints the value of the comparing_number, 0 while adding one each
time. This process continues until the value equals the value the user
entered.'''

try:
    shortcut_operator2 = int(input("\n\n4. Please enter another number 1 to "
                                   "50. "))
    comparing_number2 = 100
except ValueError:
    print("\nPlease only input numerical values.")
    shortcut_operator2 = int(
        input("\n\n4. Please enter another number 1 to "
              "50. "))
    comparing_number2 = 100

while comparing_number2 >= shortcut_operator2:
    print(comparing_number2)
    comparing_number2 -= 1
'''Constantly prints the value of the comparing number, 100 while subtracting
one each time it is executed. This process continues until the value is equal
to the number the user entered.'''


# Parameter Passing Function

def printgreaternumber(num1, num2):
    if num2 > num1:
        greater_number = num2
    else:
        greater_number = num1
    return greater_number


'''Determines the larger of the two numbers inputted by the user.'''


def printgreaternumbercall():
    num_input1 = int(input("\n\n5. Please enter a number. "))
    num_input2 = int(input("\n6. Please enter another number. "))

    greater_number = printgreaternumber(num_input1, num_input2)
    print("The larger number between your two inputs is ", greater_number)


'''Prompts the user for two numbers, compares them, and then displays the
larger of the two numbers to the user.'''

printgreaternumbercall()

# Cited Sources:

# 1. GeeksforGeeks. (2022, July 20). "Python end parameter in print()".
# GeeksforGeeks. Retrieved September 18, 2022, from
# https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

# 2. GeeksforGeeks. (2021, January 21). "Python: Sep Parameter in print()".
# GeeksforGeeks. Retrieved September 18, 2022, from
# https://www.geeksforgeeks.org/python-sep-parameter-print/

# 3. GeeksforGeeks, (2022, September 7), “Python Docstrings” GeeksforGeeks.
# Retrieved December 2, 2022, from
# https://www.geeksforgeeks.org/python-docstrings/.

# 4. w3resource, (2022, August 19), "Python if elif else" w3resource. Retrieved
# December 2, 2022 from
# https://www.w3resource.com/python/python-if-else-statements.php

# 5. w3schools, (2019, July 20), "Python Functions" w3schools. Retrieved
# December 3, 2022 from
# https://www.w3schools.com/python/python_functions.asp

# 6. trytoprogram, (2021, March 18), "Python while loop" trytoprogram.
# Retrieved December 3, 2022 from
# http://www.trytoprogram.com/python-programming/python-while-loop/

# 7. GeeksforGeeks, (2022, August 20), "Python Try Except" GeeksforGeeks.
# Retrieved December 3, 2022 from
# https://www.geeksforgeeks.org/python-try-except/
