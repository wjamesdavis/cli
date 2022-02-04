# Part 4 - While Loops

"""
If you ever find yourself in a while loop that will never end, hit ctrl+c !
"""

"""
Task - Use a while loop to print out odd numbers from 1-20
"""

i = 0

while i < 20:
    i += 1
    if i%2 != 0:
        print(i)