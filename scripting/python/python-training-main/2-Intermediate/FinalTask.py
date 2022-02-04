"""
Final Intermediate Task:
    Using what you have just learned, re-write your calculator from part 1
        to have the following functionality:
            - Allow the user to input as many numbers as they want
                - It should stop prompting for numbers when they say "stop"
            - Allow the user to specify what operation to do 
                (add, multiply, average, exit)
                - It should continue to ask what operation is to be done 
                    until the user says "exit"


Example

Input:
1
2
6
2
5
stop

Would you like to: Add, Multiply, Average, or Exit?

Input: Add

16

Input: Multiply

120

Input: Exit
"""
# import math library
import math

# create empty global list
userInputs = []
userOptions = {
    "escape": ["STOP", "EXIT"],
    "math": ["ADD", "MULTIPLY", "AVERAGE"]
}

# create global variables
inputPrompt = "Please input a series of numbers. After each number press enter. When you finish type STOP... "
choicePrompt = "Would you like to: ADD, MULTIPLY, AVERAGE, or EXIT? "
goodbye = "You chose to EXIT. Self Destruct sequence initiated... "

#function for taking input into a list
def addToList():
    print(inputPrompt)
    userNum = ""
    while userNum != userOptions["escape"][0]:
        userNum = input()
        if userNum != userOptions["escape"][0]:
            userInputs.append(int(userNum))

# function for math stuff
def interact():
    userChoice = ""
    while userChoice != userOptions["escape"][1]:
        print(choicePrompt)
        userChoice = input()
        if userChoice == userOptions["math"][0]:
            print(sum(userInputs))
        elif userChoice == userOptions["math"][1]:
            print(math.prod(userInputs))
        elif userChoice == userOptions["math"][2]:
            print(sum(userInputs)/len(userInputs))
        elif userChoice == userOptions["escape"][1]:
            print(goodbye)
        else:
            print(f"Unknown input: {userChoice}")

# running functions
addToList()
interact()
