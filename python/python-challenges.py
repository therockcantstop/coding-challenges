import operator

def get_truth(inp, relate, cut):
    ops = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne
    }
    return ops[relate](inp, cut)

____________________________________________________________________________

# Finds the median of an array

import numpy

numbers = [3,5,2]
median = numpy.median(numbers)

print("The median is:")
print(median)

_____________________________________________________________________________

# Sorting a string to print in alphabetical order
before_alph = 'ZYXWVUTSRQPONMLJKIHGFEDCBA'
after_alph = sorted(before_alph)
print(after_alph)


_____________________________________________________________________________
