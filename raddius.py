import math
import numpy as np
def Diameter(d):
    r = d/2
    return (r)

def Circumference(C):
    r = C/6.28
    return (r)

def Volume(V):
    r = V/3.14
    r = float(r)
    r = r * 0.75
    r = math.pow(r, 1/3)
    return (r)

def Surface (S):
    r = S/3.14
    r = r * 4
    r = np.sqrt(r)
    return (r)

if __name__ == "__main__":
    d = int(input("enter the diameter" ))
    print (Diameter(d))
    
    C = int(input("Enter the Circumference"))
    print (Circumference(C))
    
    V = int(input("Enter the Voume"))
    print (Volume(V))
    
    S = int(input("Enter the Surface" ))
    print (Surface(S))
    
