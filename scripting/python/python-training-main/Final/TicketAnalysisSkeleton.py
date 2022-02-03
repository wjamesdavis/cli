"""
In this project, you will be analyzing 'IT Tickets.csv'
You must first open the file in python, and convert the data into
    a format that is useful for you (E.G, lists and dictionaries)
Once this is done, do some analysis on the data.

Do at LEAST one of the following, or your own:
    - How many tickets has a single IT member owned? (Easier)
    - How many tickets have every member of IT Owned (each)? (Medium)
        - Extra: Sort these from greatest to least (Hard)

    - How many tickets has a single user sent in? (Easier)
    - How many tickets have all users sent in (each)? (Medium)
        - Extra: Sort these from greatest to least (Hard)

    - What is the average expected turnaround time (Date Expected - Date Requested) (Hard)
        - Extra: Seperate this by 'Requested By'
    - What is the average actual turnaround time (Date Completed - Date Requested) (Hard)
        - Extra: Seperate this by 'Owner'
"""


def createList(filePath):
    """
    STEP ONE
    Given the file path to the CSV of ticket data,
    Open the file, and turn it into a list where each list entry is a row in the excel file
    """

def rowToDictionary(row):
    """
    STEP TWO/THREE
    Given a single row of the CSV, convert and return that one row to a dictionary

    Hints: - The keys to the dictionaries is the top row of the CSV
           - A dictionary should look similar to:
                {..., 'Created By':<Value>, 'Created On':<Value>, ...}
           
           - The row will be separated by commas. 
                Use the string.split(',') command to split the string on every comma into a list 
    """

def createDictionaryList(ticketList):
    """
    STEP TWO/THREE
    Given a list of all the tickets, convert every line into a dictionary
    Then return that list of dictionaries

    Hint: Implement and utilize the function 'rowToDictionary' above to convert a line to a dictionary
    """


def getOwnerTicketCount(tickets, user):
    """
    STEP 4
    Given the list of dictionaries of the tickets and an IT member, 
    Calculate and return the number of tickets that member has been assigned
    """



if __name__ == "__main__":

    # Open and convert the CSV file to a list
    
    # Edit that list to convert every row into a dictionary

    # Take the user's input to see who they want statistics on

    # run and print out the statistics on the given person from the last line