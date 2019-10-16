import sys
import string

def text_analyzer(text):
    up = sum(1 for c in text if c.isupper())
    low = sum(1 for a in text if a.islower())
    punc = 0
    for b in text:
        if b in string.punctuation:
            punc += 1
    space = text.count(" ")
    print ("The text contains", up + low + punc + space, "characters:")
    print ("-", up, "upper letters")
    print ("-", low, "lower letters")
    print ("-", punc, "punctuation marks")
    print ("-", space, "spaces")
    return
