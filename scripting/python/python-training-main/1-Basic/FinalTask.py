"""
Final Beginner Task:
    Take the users input to get four numbers
    Print out the 4 numbers the user entered in one line, 
        with a sentence to remind them what they entered
    Then calculate the average, sum, and product of these numbers,
        and print out these values with an 'fstring'

Example:

Enter your 4 numbers
Number 1: 8
Number 2: 12
Number 3: 3
Number 4: 19

You entered: 8 12 3 19
The Average is: 10.5
The Sum is: 42
The Product is: 5472
"""

# Import math library
import math

# Prompt user for input
print ("Enter your 4 numbers ")
userPrompt1 = int(input("Number 1: "))
userPrompt2 = int(input("Number 2: "))
userPrompt3 = int(input("Number 3: "))
userPrompt4 = int(input("Number 4: "))

# Do all the math
userNums = [userPrompt1,userPrompt2, userPrompt3, userPrompt4]
numSum = sum(userNums)
numAvg = numSum / len(userNums)
numProd = math.prod(userNums)
numPrint = " ".join(list(map(str, userNums)))

# Print the results
print (f"You entered: {numPrint}")
print (f"The Average is: {numAvg}")
print (f"The Sum is: {numSum}")
print (f"The Product is: {numProd}")