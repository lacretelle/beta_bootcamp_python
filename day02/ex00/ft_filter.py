# list of alphabets
alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(alphabet in vowels):
        return True
    else:
        return False

def ft_filter(fnct, tab):
    """  creates a list of elements for which a function returns true. Here is a short and concise """
    res = []
    for i in tab:
        if fnct:
            if fnct(i):
                res.append(i)
        else:
            if i:
                res.append(i)
    return res

filteredVowels = filter(filterVowels, alphabets)
newvo = ft_filter(filterVowels, alphabets)

print('The filtered WITH FILTER:')
for vowel in filteredVowels:
    print(vowel)
print('The filtered WITH Ft:')
for i in newvo:
    print(i)

# random list
randomList = [1, 'a', 0, False, True, '0']

filteredList = filter(None, randomList)
fil = ft_filter(None, randomList)

print('The filtered REAL')
for element in filteredList:
    print(element)
print('The filtered FT')
for e in fil:
    print(e)

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
less = ft_filter(lambda x: x < 0, number_list)
print(less)
