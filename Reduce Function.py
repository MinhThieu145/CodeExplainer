from fractions import Fraction
from functools import reduce


def product(fracs):
    # reduce sẽ thực hiện lần lượt 2 cái 1 nhé, VD fact là [1,2,3] thì sẽ (1 * 2) * 3 
    t = reduce(lambda x,y: x*y,fracs)
    return t.numerator, t.denominator