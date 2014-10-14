@@ -0,0 +1,204 @@
from copy import deepcopy
import random
import operator
import math

global x, y, p, InputList, Tuple, WeightListInput1, WeightListInput2, WeightListHidden

p = 0.2
InputList = []
Tuple = []
WeightListInput1 = []
WeightListInput2 = []
WeightListHidden = []
ErrorList = [0,0,0,0,0,0,0]
UList = []

def SquashingFunction(x):
    return 1.0/(1 + math.exp(1)**float(-x))

#Calculate all U's - 6 first positions is the hidden the 7th is the output.
def CalculateU():
    b = 0
    #There are 7 possible U's (6 hidden + 1 output)
    for z in range(7):
        #If the U is one of the hidden
        if z <= 5:
            a = (float(x) * WeightListInput1[z] + float(y) * WeightListInput2[z])
            UList.append(a)
        #Else if the U is the output
        else:
            for w in range(6):
                b = UList[w]*WeightListHidden[w] + b
            UList.append(b)
    
    #Using the Squashing Function
    for z in range(6):
        UList[z] = SquashingFunction(UList[z])

def ComputeActivation(x,y,expected):
    for z in range(6): #6 hidden nodes
        #6 weights each input
        WeightListInput1.append(random.uniform(-1.0,1.0))
        WeightListInput2.append(random.uniform(-1.0,1.0))
        #each weight of 6 hidden
        WeightListHidden.append(random.uniform(-1.0,1.0))

        
def ComputeErrors(UList, WeightList, expected, t):
    #Output error
    if t == 1:
        d = UList[6]*(1 - UList[6])*(float(expected) - (UList[6]))
        #The 6th postion in the list represent the output node error, the first's 5 is for the hidden's node..
        ErrorList.insert(6,d)
    #hidden error
    else:
        for z in range(6):
            d = UList[z]*(1 - UList[z])*(ErrorList[6]*WeightListHidden[z])
            ErrorList[z] = d
            
def ChangeWeights(t):
    #Output weight [FLAG]
    if t == 1:
        for z in range(6):
           WeightListHidden[z] = WeightListHidden[z] + p * ErrorList[6] * UList[z]
    #Hidden weight [FLAG]
    else:
        for z in range(6):
            WeightListInput1[z] = WeightListInput1[z] + p * ErrorList[z] * float(x)
        for z in range(6):
            WeightListInput2[z] = WeightListInput2[z] + p * ErrorList[z] * float(y)
        
def BackPropagation(x,y,expected,i):
    #In the first interaction the "ComputeActivation is necessarly, after don't
    if i == 0:
        ComputeActivation(x,y,expected)

    CalculateU()

    t = 1 #Compute output error [FLAG]
    ComputeErrors(UList, WeightListHidden, expected, t)
    ChangeWeights(t)

    t = 0 #Compute hidden error [FLAG]
    ComputeErrors(UList, WeightListHidden, expected, t)
    ChangeWeights(t)


##################
    #Main        
##################
        
#Read all entries
FileName = input("Enter the name of the file with the inputs: ")
File = open(FileName)
Data = File.readlines()
FileLines = len(Data)

#Report file
a = open("a.txt", 'w')
a.write('x')
a.write(' ')
a.write('y')
a.write(' ')
a.write('excp')
a.write(' ')
a.write(' ')
a.write(' ')
a.write('error')
a.write('\n')
a.close()

#All Cases

for i in range(7):
    a = open("a.txt", 'a')
    Tuple = Data[i]

    #Sometimes the value is a unit, sometimes is a dozen.
    if Tuple[1] == " ":
        x = Tuple[0]
    else:
        x = Tuple[:2]

    #Sometimes the value is a unit, sometimes is a dozen.
    if Tuple[1] == " " and Tuple[3] == " ":
        y = Tuple[2]
    elif Tuple[2] == " " and Tuple[4] == " ":
        y = Tuple[3:4]
    elif Tuple[2] == " " and Tuple[5] == " ":
        y = Tuple[3:5]
        
    expected = Tuple[-2]

    #Calling
    BackPropagation(x,y,expected,i)

    #Saving Report
    a.write(x)
    a.write('|')
    a.write(y)
    a.write('|')
    a.write(expected)
    a.write(' ')
    a.write(' ')
    a.write('->')
    a.write(' ')
    a.write(' ')
    a.write(str(ErrorList[6]))
    a.write('\n')
    a.close()
    

    print(x)
    print(y)
    print(expected)
    print(ErrorList[6])
    print()

print('------------------------')
print("a.txt report generated.")
print('------------------------')
print()

cont = "y"
while cont != ("n" or "N"):
    cont = input("Do you want to continue with the backpropagation​? The values will be append in the report(Y/N): ")
    if cont == ("y" or "Y"):
        x = input("Insert the 'x' value: ")
        y = input("Insert the 'y' value: ")
        expected = input("Insert the 'expected' value: ")
        BackPropagation(x,y,expected,i)
        print()
        print(x)
        print(y)
        print(expected)
        print(ErrorList[6])
        print()
        a = open("a.txt", 'a')
        a.write(x)
        a.write('|')
        a.write(y)
        a.write('|')
        a.write(expected)
        a.write(' ')
        a.write(' ')
        a.write('->')
        a.write(' ')
        a.write(' ')
        a.write(str(ErrorList[6]))
        a.write('\n')
        a.close()
   



    





    
    

