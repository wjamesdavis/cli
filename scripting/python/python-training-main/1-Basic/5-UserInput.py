# Part Five - User Input

"""
userName = input("What is your name? ")
"""
##print("Your name is", userName, "and it is", userName.length, "characters long")
"""
print(f"Your name is {userName}, and it is {len(userName)} characters long")
"""

#favNumber = input("What is your favorite number? ")
#print(f"Your favorite number * 3 is {favNumber / 3}")


"""
Task - Take input from the user to get a word, and a number.
        Then print that word that number of times

E.G.
Input:
    Horse
    3
Returns:
    HorseHorseHorse


Hint: You can multiply strings by numbers to print a string that number of times
"""
userWord = input("Please type a word ")
userNum = int(input("What is your favorite number? "))

print (userWord * userNum)