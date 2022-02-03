# Part 2, Files
def getSum(filePath):
    with open(filePath, "r") as data:

        total = 0
        numbers = 0
        for line in data:
            total += int(line)
            numbers += 1

        return total


"""
The code above will open the file 'data.txt' for reading ("r"),
and save that into the variable 'data' (as data). 

The file will automatically be closed once the "with" block is left
"""


def getAverage(filePath):
    with open(filePath, "r") as data:

            total = 0
            numbers = 0
            for line in data:
                total += int(line)
                numbers += 1

            return total/numbers


if __name__ == "__main__":
    
    total = getSum("data.txt")
    avg = getAverage("data.txt")

    print(f"The total is {total}")
    print(f"The average is {avg:.2f}")
