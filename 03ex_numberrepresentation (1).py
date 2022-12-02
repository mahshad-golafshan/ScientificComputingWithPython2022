# -*- coding: utf-8 -*-
"""03ex_numberRepresentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UhBNBqGqVyzuJlixK72itUfpTWoT2pcY

#1
"""

def Converter():  
    x=input("x?")  
    origin_type=input("origin(bin,dec,hex)?") 
    destination_type=input("destination(bin,dec,hex)?") 
    if origin_type=="bin" and destination_type=="dec":   
        x_list=[int(x) for x in str(x)]
        print("output:", sum([((2**(len(x_list)-1-i)))*x_list[i] for i in range(len(x_list))]))
    elif origin_type=="dec" and destination_type=="bin":  
        x=int(x)
        temp, remain= x,0
        x_dec=[]
        while temp!=0:
            remain= temp%2
            temp= int(temp/2)
            x_dec.append(str(remain))
        x_dec.reverse()
        print("output:", int("".join(x_dec)))
    elif origin_type=="dec" and destination_type=="hex":  
        hex_dict = {10:"A",11:"B",12:"C",13:"D", 14:"E",15: "F"}  
        x=int(x)
        temp, remain= x,0
        x_dec=[]
        while temp!=0:
            remain= temp%16
            temp= int(temp/16)
            if remain<10: x_dec.append(str(remain))
            else: x_dec.append(hex_dict.get(remain))
        x_dec.reverse()
        print("output:", "".join(x_dec))
    elif origin_type=="hex" and destination_type=="dec": 
        hex_to_dec= {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        x_list=[str(x) for x in x]
        print("output:",sum([((16**(len(x_list)-1-i)))*(hex_to_dec.get(x_list[i])) for i in range(len(x_list))])) 
Converter()

"""#2"""

def converter():
    x=input("32 digit binary ?") 
    bits= [int(x) for x in list(x)]       
    sign=[+1 if bits[0]==0 else -1]      
    exponent = bits[1:9]                   
    mantissa= bits[9:]                   
    ex=sum([((2**(len(exponent)-1-i)))*exponent[i] for i in range(len(exponent))])  
    mant= 1+ sum([mantissa[i]*(2**(-i-1)) for i in range(len(mantissa))])           
    Number= sign[0] * (2**(ex-127)) * mant      
    print(Number)
converter()

"""#3"""

import math 
x1,x2=1,1          
while(x1!=0):
    last_one=x1
    x1=x1/2                                       
print("underflow:", last_one)
while(x2!=math.inf):
    last_one=x2                               
    x2=x2*2
print("overflow:",last_one)

"""#4"""

step=0.5
x1,x2=1,2
while(x1!=x2):                   
    last_one = x1                
    x1=x1+step                   
    step=step/2
print(x2-last_one)

"""#5"""

#.............PART A
import numpy as np 
def quad(a,b,c):
    x1= (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
    x2= (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
    return x1,x2
print("first:", quad(0.001, 1000, 0.001))
#..............PART B
def quadd(a,b,c):
    x1 = ((-b + np.sqrt(b**2 - 4*a*c)) * (-b - np.sqrt(b**2-4*a*c)))/((-b - np.sqrt(b**2 - 4*a*c))*(2*a))
    x2 = ((-b - np.sqrt(b**2 - 4*a*c)) * (-b + np.sqrt(b**2-4*a*c)))/((-b + np.sqrt(b**2 - 4*a*c))*(2*a))
    return x1,x2
print("seocnd:", quadd(0.001, 1000, 0.001))

"""#6"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.misc import derivative
def der(f,x,delta):    
    return (f(x+delta) - f(x))/delta
f= lambda x: x**2 - x
print(" derivate ", der(f,1, 0.01))          
print(" analytic ",derivative(f,1, 0.01))    
def accuracy(f,x,delta): 
    return (1-(np.abs((der(f,x,delta)- derivative(f,x,delta))/der(f,x,delta))))
delta_list=[10**-4, 10**-6, 10**-8, 10**-10, 10**-12, 10**-14] 
acc_list= [accuracy(f,1,delta) for delta in delta_list]    
plt.plot(delta_list, acc_list)      
plt.xlabel('delta')
plt.ylabel('Accuracy')

"""#7"""

import time
import numpy as np
#..............PART A
y= lambda x: np.sqrt(1-x**2)
N=100
h=2/N          
I=0            
x=-1           
for i in range(N): 
    I+= h*y(x)
    x+= h
print(I)
print(np.pi/2)
#..............PART B
n=900000 
t=0      
while(t<1):   
    h=2/n
    I=0
    x=-1
    start = time.time()
    for i in range(n): 
        I+= h*y(x)          
        x+= 2/n
    end = time.time()
    t=end - start
    n+=1000                 
print(n)
start =time.time()
y= lambda x: np.sqrt(np.abs(1-x**2))
N=35000000   
h=2/N
I=0
x=-1
for i in range(N): 
    I+= h*y(x)
    x+= h
print("\n")
end = time.time()
print(N)
#print(format(end-start))