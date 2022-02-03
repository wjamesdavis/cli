def combine(a, b):
    result = a + b
    return result


if __name__ == "__main__":
    print("I'm in main!")


"""
Notice how 'combine' does not run, but line 6 does
Line 6 is how python does it 'main' entry point- where code starts executing

You can still just place code 'out in the open' as we have been previously,
but this is considered bad practice, and should be avoided when possible.

All code should be either inside a function, or inside 'main'
"""