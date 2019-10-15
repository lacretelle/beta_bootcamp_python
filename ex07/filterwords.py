import sys
import string

argm = sys.argv
argm.reverse()
if argm[0] == "filterwords.py":
    print ('ERROR')
    exit()
elif argm[1] == "filterwords.py":
    print ('ERROR')
    exit()
elif argm[2] != "filterwords.py":
    print ('ERROR')
    exit()
else:
    argm.reverse()
    if isinstance(argm[1], str):
        if argm[2].isdigit():
            lst = argm[1].split()
            print (lst)
        else:
            print ('ERROR')
    else:
        print ('ERROR')

