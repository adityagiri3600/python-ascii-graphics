from math import*

#vectors
#region
class vec: #vector class

    def __init__(self,*args):
        if len(list(args))!=1:
            self.component = list(args)
        else:
            self.component = args[0]
        self.magnitude = magnitude(self)
        self.dim = dim(self)
        self.i = self.x = self.component[0]
        self.j = self.y = self.component[1]
        if self.dim > 2:
            self.k = self.z = self.component[2]

    def __add__(self,other):

        check_if_vector(other) #checks if we're adding vectors
        if self.dim != other.dim:        #checks if dimensions of the vectors we're adding are same
            raise TypeError(f"dimensions of {self} and {other} don't match")

        return vec([self.component[i] + other.component[i] for i in range(len(self.component))]) 
    def __sub__(self,other):

        check_if_vector(other) #checks if we're adding vectors
        if self.dim != other.dim:        #checks if dimensions of the vectors we're adding are same
            raise TypeError(f"dimensions of {self} and {other} don't match")

        return vec([self.component[i] - other.component[i] for i in range(len(self.component))]) 

    def __mul__(self, other):
        return vec([other*self.component[i] for i in range(len(self.component))])

    def __truediv__(self, other):
        return vec([self.component[i]/other for i in range(len(self.component))])

    def __neg__(self):
        return vec([-self.component[i] for i in range(len(self.component))])

    def __eq__(self,other):
        res = True
        for i in range(len(self.component)):
            res &= self.component[i]==other.component[i]
        return res

    def __ne__(self,other):
        return not self==other

    def __str__(self): #tells how to print a vector
        return "(" + ','.join(map(str,self.component)) + ")"

def check_if_vector(x): #checks if we're adding vectors
    if(type(x)!=vec):
        raise TypeError(f"{x} is not a vector")

def dot(vector1,vector2): #dotproduct
    check_if_vector(vector1)
    check_if_vector(vector2)
    return sum(vector1.component[i]*vector2.component[i] for i in range(len(vector1.component)))

def dim(vector): #gives the dimension of the vector
    check_if_vector(vector)
    return len(vector.component)

def magnitude(vector):
    check_if_vector(vector)
    return sqrt(dot(vector,vector))

def normalize(vector): #returns a unit vector in the direction of x
    check_if_vector(vector)
    return vector/vector.magnitude

def cross(vector1,vector2):
    a = vector1
    b = vector2
    check_if_vector(a)
    check_if_vector(b)
    if a.dim != 3:
        raise Exception("cross product is only defined for 3 dimensional vectors")
    if b.dim != 3:
        raise Exception("cross product is only defined for 3 dimensional vectors")
    x = a.component[1]*b.component[2]-b.component[1]*a.component[2]
    y = a.component[2]*b.component[0]-b.component[2]*a.component[0]
    z = a.component[0]*b.component[1]-b.component[0]*a.component[1]
    return vec(x,y,z)
#endregion

def derivative(f):
    def d(x):
        h = 0.00000000001
        D = f(x+h)/h - f(x)/h
        if type(f(0)) != vec:
            return round(D,4)
        else:
            return vec([round(D.component[i],4) for i in range(f(0).dim)])
    return d