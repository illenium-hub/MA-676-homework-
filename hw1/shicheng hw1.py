#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:40:52 2020

@author: shichengwang
"""
import math

# Q1:
## (a)
list_a = []
a = 20
i=0
while i>=0:
    i = i+1
    list_a.append(i)
    if i >= 20:
        break
print(list_a)    ## list shows as a list.
  

## (b)
list_b = []
i=21
while i>=0:
    i = i-1
    list_b.append(i)
    if i < 2:
        break
print(list_b)  

## also could reverse list_a
# list_a.reverse()
# print(list_a)

## (c)
i=20
while i>=0:
    i = i-1
    list_a.append(i)
    if i<2:
        break
print(list_a)

## (d)
list_c = [4,6,3]
print(10 * list_c) 

## (e)
list_d = [4,6,3]*11
del list_d[31:33]
print(list_d)


# Q2
### define a function
def fun2(a):
    return math.exp(a) * math.cos(a)
### start the loop
list_2=[]
x=2.9
while x>=2.9:
    x = x+0.1
    y = fun2(x)
    list_2.append(y)
    if x>5.9:
        break
print(list_2)
        
# Q3
### define a function
def fun3(b):
    return 2**(b)/b
### start the loop
list_3=[]
x=0
while x>=0:
    x = x+1
    y = fun3(x)
    list_3.append(y)
    if x > 24:
        break
print(list_3)

# Q4
## (a)
list_c = []
c = 19
i=0
while i>=0:
    i = i+1
    list_c.append(i)
    if i > 19:
        break
print(list_c) 

list_4=[]
for i in range(20):
    j = list_c[i]-list_c[19-i]
    list_4.append(j)
print(list_4)
    
## (b)
list_4 = []
for i in range(20):
    if  list_c[i]%2 == 0:
        j = True      
        list_4.append(j)    ### recognize the even number 
    else: 
        j = False 
        list_4.append(j)    ### count the odd number 
print(list_4)



# Q5
## (a)       
### import the data 
data = open("/Applications/BU/BU 2/676 Statistical Practice II/discussion/hw1/lorem.txt","r")
text = data.read(); ### read the data

### start the count
count = 0
count_total = 0
lst = text.split()  ### spilt text into words

### start the loop
for i in lst:
    if len(i) >= 1 and len(i) <= 4:
        count += 1
print(count)



## (b)
lst = text.split()
### start counting
count = 0
### start looping
for i in text:
    for j in i:
        if j.isupper():
            count += 1
print(count)





































