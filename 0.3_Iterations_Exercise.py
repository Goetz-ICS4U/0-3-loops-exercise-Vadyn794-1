"""
author: Vadyn794
date: 2026/02/15
0.3 - Repetition Review Exercises
"""

# Task 1: Write a program to calculate the factorial of any number that the user enters using a loop. Ex. 5! = 5*4*3*2*1 = 120
# Your code goes here
x = int(input("Enter value: "))
value = 1

for i in range(1, x + 1):
    value = value * i
    print(value)

if x == 0:
    print(1)
# Task 2a: Write a program that asks for five marks and computes the average, rounded to 1 decimal place.
# Your code goes here
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))

lst = [a, b, c, d, e]

total = sum(lst)
length = len(lst)
average = total/length

print(f"{average:.1f}")

# 2b)  Modify the program from task 2a to also output the lowest and highest mark WITHOUT lists.
# Your code goes here
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))

average = (a + b + c + d + e) / 5

highest = max(a, b, c, d, e)
lowest = min(a, b, c, d, e)

print(f"Average: {average:.1f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")

# 2c)  Modify the program from task 2b to check if the mark entered is between 0 and 100. Keep asking user for input until they give a valid grade.
# Your code goes here

total = 0
highest = -1   
lowest = 101 

for i in range(0, 5):
    while True:
        mark = int(input(f"Enter mark {i} (0-100): "))
        
        if 0 <= mark <= 100:
            break
        else:
            print("Invalid input. Mark must be between 0 and 100")

    total = total + mark
    
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

average = total / 5

print(f"Average: {average:.1f}")
print(f"Highest Mark: {highest}")
print(f"Lowest Mark: {lowest}")

# 2d)  Modify the program to ask the user to enter -1 when done entering marks.
# Your code goes here
total = 0
count = 0
highest = -1
lowest = 101

while True:
    mark = int(input("Enter mark (-1 to stop): "))

    if mark == -1:
        break

    if 0 <= mark <= 100:
        total += mark
        count += 1

        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
    else:
        print("Invalid number")

if count > 0:
    average = total / count
    print(f"Average: {average:.1f}")
    print(f"Highest Mark: {highest}")
    print(f"Lowest Mark: {lowest}")
else:
    print("No entered marks")


# Task 3a) Determine the largest of n positive integers entered the user.
# The program should loop until a negative value is read (aka, use Sentinel Value).
# Your code goes here
largest = -1
print("Enter positive integers. Enter a negative number to stop")

while True:
    inp = int(input("Enter value: "))

    if inp < 0:
        print("The value must be positive")
        break
    
    if inp > largest:
        largest = inp

if largest >= 0:
    print(f"The largest number entered was: {largest}")
else:
    print("No positive numbers were entered")

# 3b) Modify the program to find the two largest integers.
# Your code goes here
largest = -1
second_largest = -1

print("Enter positive integers. Enter a negative number to stop")

while True:
    inp = int(input("Enter value: "))

    if inp < 0:
        break
    
    if inp > largest:
        second_largest = largest
        largest = inp
    
    elif inp > second_largest:
        second_largest = inp

if largest != -1:
    print(f"The largest number was: {largest}")
    if second_largest != -1:
        print(f"The second largest number was: {second_largest}")
    else:
        print("Only one number was entered")
else:
    print("No positive numbers were entered")

# Task 4) Use the random module to choose a number between 1 and 100.
# Then print all the factors of that number.
# Ask the user if they wish to play again – loop until the user enters “No” (sentinel value).
# Your code goes here
import random

play_again = "yes"

while play_again.lower() == "yes":
    randomizer = random.randint(1, 100)
    print(f"The randomizer chose number: {randomizer}")
    print(f"The factors of {randomizer} are:")

    for i in range(1, randomizer + 1):
        if randomizer % i == 0:
            print(i)

    play_again = input("Would you like to play again? (Yes/No): ")

print("Ok, see you next time")

# Task 5) One useful technique when analyzing a number is to use a loop and the modulus operator to extract each digit 
# from the end.
# Consider this code:

num = int(input("Enter a positive integer: "))

while (num >= 1):
    digit = num % 10
    num = num//10
    print(digit)

# Use this above code to do the following:
# Count the number of sevens in a positive integer.

num = int(input("Enter a positive integer: "))

count_seven = 0

while num >= 1:
    digit = num % 10
    
    if digit == 7:
        count_seven = count_seven + 1
    
    num = num // 10

print(f"Number of sevens: {count_seven}")

# Count the number of odd digits, and the number of even digits, in a positive integer.

num = int(input("Enter a positive integer: "))

odd_count = 0
even_count = 0

while num >= 1:
    digit = num % 10
    
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    num = num // 10

print(f"Number of odd digits: {odd_count}")
print(f"Number of even digits: {even_count}")



