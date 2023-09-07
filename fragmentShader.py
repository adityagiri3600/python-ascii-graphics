import shapes
from math import*
from my_functions import*

asc = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\/|()1{}[]?-_+~<>i!lI;:,^`'. "
ln = len(asc)
def ascf(num):
    return asc[floor(ln*min(1,num))-1]

def fragment(x,y):
    if shapes.circle(x,y,0,0,10):
        return ascf(0.5)
    else:
        return ascf(1)
