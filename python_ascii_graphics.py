#from fragmentShader import*
import os
import time
import shapes
from math import*
from Calculus import*

WIDTH = 235
HEIGHT = 65
CAMERA = vec(0,0,5)
shiftX = 0
shiftY = 0
my_time = 0

buffer_1 = ""

asc = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\/|()1{}[]?-_+~<>i!lI;:,^`'. "
ln = len(asc)
def ascf(num):
    return asc[ceil(ln*min(1,num))-1]

def ray_march(ro,rd):
    fd = 0
    for i in range(4):
        p = ro + rd*fd
        d =  min(10000,magnitude(vec(0,30,20)-p)-10)
        fd += d
        if d<0.1: break
    return fd

def fragment(x,y):
    #if shapes.circle(x,y,30*cos(0.1*my_time),30*sin(0.1*my_time),10):
    #    return ascf(0.5)
    #else:
    #    return ascf(1)
    d = ray_march(CAMERA,vec(x,1,y))
    return ascf(abs(d/500000))

while my_time==0:
    time.sleep(0.01)
    os.system('cls')
    print(buffer_1)
    buffer_1 = ""
    for row in range(HEIGHT):
        for column in range(WIDTH):
            print(fragment(column-WIDTH/2 - shiftX, 2.1*(-row+HEIGHT/2)-shiftY),end="")
        print("")
    my_time += 1
