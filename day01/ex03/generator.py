import random

def generator(text, sep=" ", option=None):
    if text:
        lst = text.split(sep)
        if option == "shuffle":
            random.shuffle(lst)
        elif option == "unique":
            lst = list(dict.fromkeys(lst))
        elif option == "ordered":
            lst.sort()
        for i in lst:
            yield i
    else:
        print ("Error.")
        exit()
