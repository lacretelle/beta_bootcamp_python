import sys
import math

arguments = len(sys.argv)
if arguments > 2 :
    print ("ERROR")
elif arguments == 2:
    nb = sys.argv[1]
    if nb.isdigit() == True:
        nb = int(nb)
        if nb == 0:
            print ("I'm Zero.")
        elif nb % 2 == 0:
            print ("I'm Even.")
        else:
            print ("I'm Odd.")
    else:
        print ("ERROR")
