# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:27:36 2018

@author: HP
"""

# Assignment 2 - Data Science Masters

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

values = input("Input some comma seprated numbers : ")
l=values.split(",")
print (l)
type (l)

# . Create the below pattern using nested for loop in Python¶

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
    

# 3. Write a Python program to reverse a word after accepting the input from the user.
# Sample Output: Input word: AcadGild Output: dilGdacA

Inputword = input ("Type Input Word : ")
print ("Input Word:" + " " + Inputword)
print ("Output:" + " " + Inputword[::-1])

# 4. Write a Python Program to print the given string in the format specified in the sampleoutput.¶

# Method1 

print ("WE, THE PEOPLE OF INDIA,"+ 
       "\n      having solemnly resolved to constitute India into a SOVEREIGN, !" + 
       "\n\t    SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC"+ 
       "\n\t     and to secure to all its citizens")
       
 # Method 2

string = """
WE, THE PEOPLE OF INDIA,  
      having solemnly resolved to constitute India into a SOVEREIGN, !  
            SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC  
             and to secure to all its citizens
"""
print(string)