# Part 4, Try, Except, and Finally

def combine(a, b):
    result = a + b
    return result


if __name__ == "__main__":

    try:
        a, b = "abc", 123
        res = combine(a, b)       
        print(f"The result is {res}")
    except:
        print(f"Failed to combine {a} {b}")
    finally:
        print("Try-Except is complete")