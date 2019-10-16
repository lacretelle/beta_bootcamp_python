def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

def ft_map(fct, tab):
    """ function map() returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc..) """
    res = []
    for i in tab:
        res.append(fct(i))
    return res

map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)
m = ft_map(to_upper_case, 'abc')
print(type(m))
print_iterator(m)

list_numbers = [1, 2, 3, 4]

it = map(lambda x: x * 2, list_numbers)
print_iterator(it)
mp = ft_map(lambda x: x * 2, list_numbers)
print_iterator(mp)
