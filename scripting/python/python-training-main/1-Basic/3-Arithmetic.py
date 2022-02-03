# Part Three- Basic Variable arithmatic and math
myInt1 = 20
myInt2 = 6

# Add and Subtract
addExample = myInt1 + myInt2
subExample = myInt1 - myInt2

# Multiply and Divide(s)
multExample = myInt1 * myInt2
floatDivExample = myInt1 / myInt2
intDivExample = myInt1 // myInt2

# Exponents
expExample = myInt1 ** 2

# Modulo (Remainder)
modExample = myInt1 % 3

# Order of Operations
pemdasExample = (myInt1 + myInt2) * 5

# Other
cat = 5
cat += 3

# Non-Number Arithmetic
twoWords = "Cat" + "Dog"
threeHorses = "Horse" * 3

"""
Task 1 - Print out the variables:
        - addExample
        - floatDivExample
        - intDivExample
        - modExample
        - threeHorses
        - twoWords
"""
print (addExample)
print (floatDivExample)
print (intDivExample)

"""
Task 2 - Find the average of 14, 12, 32, 82, 17, and print the result
"""
myNums = [14,12,32,82,17]
myAvg = sum(myNums) / len(myNums)
print (myAvg)
