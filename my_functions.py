from math import*

def dist(x,y):
    if not len(x)==3:
        return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    else:
        return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2)

def rotate(x,t):
    return (x[0]*cos(t)-x[1]*sin(t),x[0]*sin(t)+x[1]*cos(t))