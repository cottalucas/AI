@@ -0,0 +1,240 @@
#Cotta Lucas

import math
import itertools
import random
import sys
from copy import deepcopy


Vector = []
BinaryVector = []
SumOfAllVec = []
ADP = [] #All Dot Products

NormalizedVector = []
O_Normalized = []
I_Normalized = []
L_Normalized = []
Underline_Normalized = []
E_Normalized = []
X_Normalized = []

O_BinVec = []
I_BinVec = []
L_BinVec = []
Underline_BinVec = []
E_BinVec = []
X_BinVec = []
ERROR_BinVec = []

NoisyVector = []
O_Noisy = []
I_Noisy = []
L_Noisy = []
Underline_Noisy = []
E_Noisy = []
X_Noisy = []
ERROR_Noisy = []

def Matrix():
    global O, I, L, Underline, E, X, ERROR

    O = [ [1,  1,  1,  1, 1],
          [1, -1, -1, -1, 1],
          [1, -1, -1, -1, 1],
          [1, -1, -1, -1, 1],
          [1,  1,  1,  1, 1]]

    I = [ [-1, -1, 1, -1, -1],
          [-1, -1, 1, -1, -1],
          [-1, -1, 1, -1, -1],
          [-1, -1, 1, -1, -1], 
          [-1, -1, 1, -1, -1]]

    L = [ [1, -1, -1, -1, -1],
          [1, -1, -1, -1, -1],
          [1, -1, -1, -1, -1],
          [1, -1, -1, -1, -1],
          [1,  1,  1,  1, 1]]

    Underline = [ [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [ 1,  1,  1,  1,  1]]

    E = [  [1,  1,  1,  1,  1],
           [1, -1, -1, -1, -1],
           [1,  1,  1,  1,  1],
           [1, -1, -1, -1, -1],
           [1,  1,  1,  1,  1]]

    X = [  [ 1, -1, -1, -1,  1],
           [-1,  1, -1,  1, -1],
           [-1, -1,  1, -1, -1],
           [-1,  1, -1,  1, -1],
           [ 1, -1, -1, -1,  1]]

    ERROR = [   [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1]]
    
   


def BinaryVector(BinaryVector, Pattern): 
    for x in range(5):
        for y in range(5):
            BinaryVector.append(Pattern[x][y])

def Normalize(NormalizedVector, BinaryVector):
    FirstStep = 0  
    for x in range(25):
        #Finding the lenght - Numer^2 
        FirstStep = BinaryVector[x]*BinaryVector[x] + FirstStep

    #Finding the lenght - square root 
    SecondStep = math.sqrt(FirstStep)

    #Divide each components by its length.
    for x in range(25):
        NormalizedVector.append(BinaryVector[x]/SecondStep)

    #Put all normalized vectors in a list for use in the future combinations
    AN.append(NormalizedVector)
        

def DotProduct(NormalizedVector1, NormalizedVector2):
    Product = 0
    #All doct products
    for x in range(25):
        Product = NormalizedVector1[x]*NormalizedVector2[x] + Product
    ADP.append(Product)

#Create the noisy - about 20%
def Noisy(BinaryVector, NoisyVector):
    #Creating the noisy
    for x in range(25):
        NoisyVector.append(BinaryVector[x])
    #20% each position
    for x in range(25):
        a = random.randint(0,4)
        if a == 0:
            if NoisyVector[x] == 1:
                NoisyVector[x] = -1
            else:
                NoisyVector[x] = 1

def DistributedMemory():
    for x in range(25):
        A = O_BinVec[x]+ O_BinVec[x] + I_BinVec[x] + L_BinVec[x] + Underline_BinVec[x] + E_BinVec[x] + X_BinVec[x]
        SumOfAllVec.append(A)

def PrintPattern(Vector):
    for x in range(25):
            if Vector[x]== 1:
                Vector[x] = 'O '
            else:
                Vector[x] = '. '
    for y in range(25):
        if y%5 == 0:
            print()
        sys.stdout.write(Vector[y])
    
#main

#Start the patterns
Matrix()

#Construction of binary vectors
BinaryVector(O_BinVec, O)
BinaryVector(I_BinVec, I)
BinaryVector(L_BinVec, L)
BinaryVector(Underline_BinVec, Underline)
BinaryVector(E_BinVec, E)
BinaryVector(X_BinVec, X)
BinaryVector(ERROR_BinVec, ERROR)

#Dont required anymore
'''#Normalize all vectors 
Normalize(O_Normalized, O_BinVec)
Normalize(I_Normalized, I_BinVec)
Normalize(L_Normalized, L_BinVec)
Normalize(Underline_Normalized, Underline_BinVec)
Normalize(E_Normalized, E_BinVec)
Normalize(X_Normalized, X_BinVec)'''

#Noisy the vectors
Noisy(O_BinVec, O_Noisy)
Noisy(I_BinVec, I_Noisy)
Noisy(L_BinVec, L_Noisy)
Noisy(Underline_BinVec, Underline_Noisy)
Noisy(E_BinVec, E_Noisy)
Noisy(X_BinVec, X_Noisy)
Noisy(ERROR_BinVec, ERROR_Noisy)

#Create the distribuite memory
DistributedMemory()
print('Sum')
print(SumOfAllVec)
print()

#DotProduct
DotProduct(O_Noisy, SumOfAllVec)
DotProduct(I_Noisy, SumOfAllVec)
DotProduct(L_Noisy, SumOfAllVec)
DotProduct(Underline_Noisy, SumOfAllVec)
DotProduct(E_Noisy, SumOfAllVec)
DotProduct(X_Noisy, SumOfAllVec)
DotProduct(ERROR_Noisy, SumOfAllVec)
print('All dot product')
print(ADP)


print()
print('O noisy pattern')
PrintPattern(O_Noisy)
print()
print()
print('I noisy pattern')
PrintPattern(I_Noisy)
print()
print()
print('L noisy pattern')
PrintPattern(L_Noisy)
print()
print()
print('Underline noisy pattern')
PrintPattern(Underline_Noisy)
print()
print()
print('E noisy pattern')
PrintPattern(E_Noisy)
print()
print()
print('X noisy pattern')
PrintPattern(X_Noisy)
print()
print()
print('ERRORR noisy pattern')
PrintPattern(ERROR_Noisy)


#end











    


