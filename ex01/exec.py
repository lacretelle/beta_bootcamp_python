import sys

def reverse_slicing(s):
    return s[::-1]

for arg in sys.argv:
    if arg != sys.argv[0]:
        print (reverse_slicing(arg).swapcase())
