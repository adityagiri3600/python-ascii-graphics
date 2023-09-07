from math import*
from my_functions import*

def circle(x,y,x0,y0,r):
    if (x-x0)**2 + (y-y0)**2 <= r**2:
        return True
    else:
        return False

def line(x,y,a,b,t):
    A= (b[1]-a[1])/(b[0]-a[0]+0.0001)
    B= -1
    C= A*-a[0]+a[1]
    d= abs(A*x+B*y+C)/sqrt(A**2+B**2)
    if d <= t and dist([x,y],a) <= dist(a,b)+t and dist([x,y],b) <= dist(a,b)+t:
        return True
    else:
        return False