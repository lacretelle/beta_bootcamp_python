from functools import reduce

def ft_reduce(fnct, seq):
    """ function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list.  """
    first = seq[0]
    for i in seq[1:]:
        first = fnct(first, i)
    return first

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)
prod = ft_reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(prod)
