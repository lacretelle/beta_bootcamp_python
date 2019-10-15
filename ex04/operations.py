import sys

def add(a,b):
    res = int(a + b)
    return res

def diff(a, b):
    res = int(a - b)
    return res

def prod(a, b):
    res = int(a * b)
    return res

def quot(a, b):
    res = a / b
    return res

def mod(a, b):
    res = int(a % b)
    return res

num = len(sys.argv)

if num > 3 or num <= 1 :
    print ("Usage: operations.py <number1> <number2>")
    print ("Example: python operations.py 10 3")
else:
    nb1 = sys.argv[1]
    nb2 = sys.argv[2]
    if nb1.isdigit() == True:
        if nb2.isdigit() == True:
            nb1 = float(nb1)
            nb2 = float(nb2)
            print ("Sum:", add(nb1, nb2))
            print ("Difference:", diff(nb1, nb2))
            print ("Product:", prod(nb1, nb2))
            print ("Quotient:", quot(nb1, nb2))
            print ("Remainder:", mod(nb1, nb2))
