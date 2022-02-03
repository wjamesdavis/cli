# Part 5- Lists

"""
Task- Take in 3 inputs from a user, and add them all into a list.
        Then print out the list in reverse order
"""

def revList(userList) :
        userList.reverse()
        print(userList)

print("Please enter 3 words... ")

userInput = [
        input("First thing: "),
        input("Second thing: "),
        input("Third thing: ")
]

revList(userInput)