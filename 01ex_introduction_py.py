# -*- coding: utf-8 -*-
"""01ex_introduction.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C7aJ9xCmy3wbY12iphTELhINKDpugW25

#1
"""

#............PART A
l=[]
for i in range(1,101):
   if i % 15==0:
      i = 'HelloWorld'
      print(i)
      l.append(i);
   elif i % 3==0:
      i = 'Hello'
      print(i)
      l.append(i)
   elif i % 5==0:
      i = 'World'
      print(i)
      l.append(i)
   else:
      print(i)
      l.append(i)
a = tuple(l)
print(a)
#............PART B
l=list(a)
for i in range(len(l)):
    if l[i] == 'Hello':
        l[i] = 'Python'

    if l[i] == 'World':
        l[i] = 'Work'
  
b= tuple(l)
print(b)

"""#2"""

print("n?")
n=input('')
print("m?")
m=input('')
n, m = m, n
print("n=",n)  
print("m=",m)

"""#3"""

import math
a=input( )
b=input( )
def cal_dis(a,b):
   p1 = a.split(",")
   p2 = b.split(",")
   distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
   return(distance) 
print(cal_dis(a,b))

"""#4"""

s=input('given string is:')
c=input('which char?')
def count(s, c) :
    res = 0
    for i in range(len(s)) :
        if (s[i] == c):
            res = res + 1
    return res
print(count(s, c))

"""#5

"""

l = [36, 45, 58, 3, 74, 96, 64, 45, 31, 10, 24, 19, 33, 86, 99, 18, 63, 70, 85,
  85, 63, 47, 56, 42, 70, 84, 88, 55, 20, 54, 8, 56, 51, 79, 81, 57, 37, 91,
  1, 84, 84, 36, 66, 9, 89, 50, 42, 91, 50, 95, 90, 98, 39, 16, 82, 31, 92, 41,
  45, 30, 66, 70, 34, 85, 94, 5, 3, 36, 72, 91, 84, 34, 87, 75, 53, 51, 20, 89, 51, 20]
 count = 0
 s=[]
 for item in l:
     if item not in s:
          count += 1
          s.append(item)
 print(s)
 print(len(s))

"""#6"""

#int, float, str
n=input()
m=input()
#s=int(n)+int(m)
if isinstance(n, (int, float)):
  if isinstance(m, (int, float)):
    s=float(n)+float(m)
    print(s)
else:
    s=n+m
    print(s)

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

def check_user_input(input):
    try:
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")

input1 = input("Enter your int/float or str ")
check_user_input(input1)

input2 = input("Enter Enter your int/float or str ")
check_user_input(input2)

print(float(input1)+float(input2))

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)

"""#7

#for loop
"""

res = []
for i in range(0,11):
    res.append(i*i*i)
print(res)

"""#list comperhension"""

res = [i**3 for i in range(0,11)]
print(res)

"""#8"""

e=[]
[e.append((i,j)) for i in range(3) for j in range (4) ]
print(e)

a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

"""#9

"""

s=[]
c, m = 0, 2
while c < 100 :
        for n in range(1, m) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > 100 :
                break
            s.append((a,b,c))
        m = m + 1
a=tuple(s)       
print(a)

"""#10"""

import math
n=input()
for i in range(int(n)):
 vector = input().split()
 sum = 0
 for x in vector:
   x = int(x)
   x = x**2
   sum += x
 for y in range(len(vector)):
   vector[y] = int(vector[y])
   vector[y] = vector[y] / math.sqrt(sum)
print(vector)

"""#11 fib"""

count=0
n1, n2 = 0, 1
while count < 20:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1