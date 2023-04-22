##Task3 - DATA STRUCTURES

#1. Create a list of 10 elements of four different data types like int, string, complex and float.
'''
list1=[4,8,"Pranitha","ConsultAdd",3+4j,5+6j,5.4,3.7,99,36]
print(list1)
'''
#2.Create a list of size 5 and execute the slicing structure 
'''
list1=[2,4,6,8,10]
print(list1[2::])
'''
#3.Write a program to get the sum and multiply of all the items in a given list.
'''
import math
list1=[2,3,4,5,6,7]
print(sum(list1))
print(math.prod(list1))
'''
#4.Find the largest and smallest number from a given list.
'''
list1=[12,4,26,7,88,48]
print(max(list1))
print(min(list1))
'''
#5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list
'''
list1=[33,2,54,79,85,48,72,41]
#list2=[i for i in list1 if i%2!=0]
#print(list2)
list2=[]
for i in list1:
    if i%2!=0:
        list2.insert(len(list2),i)
print(list2) 
'''
#6. Create a list of elements such that it contains the squares of the first and last 5 elements between
    #1 and30 (both included).
'''
list1=[]
for i in range(1,31):
    list1.append(i**2)
print(list1[:5])
print(list1[-5:])
'''
#7.Write a program to replace the last element in a list with another list.
'''
list1=[1,3,5,7,9,10]
list2=[2,4,6,8]
list1.pop()
list1.extend(list2)
print(list1)
'''
#8.Create a new dictionary by concatenating the following two dictionaries:
'''
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
'''
#9.Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
   #and n(both 1 and n included).
'''
dict1={}
for i in range(1,6):
    dict1[i]=i**2
print(dict1)
'''
#10.Write a program which accepts a sequence of comma-separated numbers from console and
    #generates a list and a tuple which contains every number in the form of string.
'''
User_Input=input("Enter the sequence of number: ")
Refined_Input=User_Input.split(',')
list1=list(Refined_Input)
Tup1=tuple(Refined_Input)
print(list1,Tup1)
'''
##Task 4 - TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS & HIGHER ORDER FUNCTIONS

#1.Write a program to reverse a string.

#String1="1234abcd"
#print(String1[::-1])
'''
def reverse(String1):
    print(String1[::-1])
String1=reverse("1234abcd")
'''
#2.Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
'''
def UPPER_LOWER(String1):
    UPPER=0
    LOWER=0
    for i in String1:
        if i.isupper():
            UPPER+=1
        elif i.islower():
            LOWER+=1
    print("Number of UpperCase letters in string are: ",UPPER)
    print("Number of LowerCase letters in string are: ",LOWER)
String1=UPPER_LOWER("abcSdefPghijQkl")
'''
#3.Create a function that takes a list and returns a new list with unique elements of the first list.
'''
def Unique_List(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(list2)
list1=Unique_List([2,3,4,5,5,6,7,8,8])
'''
#4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words
   #in a hyphen-separated sequence after sorting them alphabetically.
'''
User_Input=input("Please enter a sentence with hyphen-separated: ")
print(User_Input)
Modified_Input=User_Input.split("-")
Modified_Input.sort()
print("-".join(Modified_Input))
'''
#5.Write a program that accepts a sequence of lines as input and prints the lines after making all
   #characters in the sentence capitalized.
'''
User_Input="Hello world Practice makes man perfect"
print(User_Input)
Modified_Text=User_Input.upper()
print(Modified_Text)
'''
#6.Define a function that can receive two integral numbers in string form and compute their sum and
   #print it in the console.
'''
def Sum():
    num1=input("Enter 1st num: ")
    num2=input("Enter 2nd num: ")
    Addition=int(num1)+int(num2)
    print(Addition)
Sum()
'''
#7.Define a function that can accept two strings as input and print the string with the maximum length
   #in the console. If two strings have the same length, then the function should print both the strings line
   #by line.
'''
def Max_Length():
    String1=input("Enter the String1: ")
    String2=input("Enter the String2: ")
    if len(String1)>len(String2):
        print(String1)
    elif len(String1)<len(String2):
        print(String2)
    elif len(String1)==len(String2):
        print(String1+"\n"+String2)
Max_Length()
'''
#8.Define a function which can generate and print a tuple where the values are square of numbers
   #between 1 and 20 (both 1 and 20 included).
'''
def Squares():
    list1=[]
    for i in range(1,21):
        list1.append(i**2)
    print(tuple(list1))
Squares()
'''
#9.Write a function called showNumbers that takes a parameter called limit. It should print all the
   #numbers between 0 and limit with a label to identify the even and odd numbers.
'''
def ShowNumber(limit):
    list1=[]
    for i in range(limit+1):
        list1.append(i)
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
limit=ShowNumber(3)
'''
#10.Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
'''
Evens=list(filter(lambda i:i%2==0, range(1,21)))
print(Evens)
'''
#11.Write a program which uses map() and filter() to make a list whose elements are squares of even numbers
'''
list1=[1,2,3,4,5,6,7,8,9,10]
Evens=list(filter(lambda i:i%2==0, list1))
print(Evens)
Squares=list(map(lambda i:i**2, Evens))
print(Squares)
'''
#12.Write a function to compute 5/0 and use try/except to catch the exceptions.
'''
def Division(a,b):
    try:
        result=a//b
        print(result)
    except Exception as e:
        print(e)
Division(5,0)
'''
#13.Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
'''
from functools import reduce
list1=[1,2,3,4,5,6,7]
Flatten=reduce(lambda a,b:10*a+b,list1)
print(Flatten)
'''
#14.Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
    #Make sure to use only higher order functions.
'''
def Multiple(num):
    if num%7==0:
        print(f"{num} number is not divisible by 3 but it is multiple of 7")
        return num
    else:
        print("Num didnt supported by Divisible function so Multiple function cannot do it")
def Divisible(num):
    if num%3!=0:
        return num
    elif num%3==0:
        print(f"{num} Number is divisible by 3")
        quit()
        return num 
print(Multiple(Divisible(49)))
'''
#15.Write a program in Python to multiply the elements of a list by itself using a traditional function
    #and pass the function to map() to complete the operation
'''
def Mul(n):
        return n*n
list1=[1,2,3,4,5,6,7,8]
Mul_List=(map(Mul,list1))
print(list(Mul_List))
'''
'''
def Self_Multiply(list1):
    list2=[i*i for i in list1]
    print(list2)
'''
'''
    list2=[]
    for i in list1:
        list2.append(i*i)
    print(list2)
'''
'''
list1=Self_Multiply([1,2,3,4,5,6,7,8])
'''
'''
list1=[1,2,3,4,5,6,7,8]
print(list1)
Multiply=list(map(lambda i:i*i,list1))
print(Multiply)
'''
#16.What is the output of the following codes:
'''
def foo(): 
    try: 
        return 1 
    finally: 
        return 2
k = foo()
print(k)
    # Output: 2
'''
'''
def a(): 
    try: 
        f(x, 4) 
    finally: 
        print('after f') 
        print('after f?')
a()
    #output: after f, after f?
'''


















        





