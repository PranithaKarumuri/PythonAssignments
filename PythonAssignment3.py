##Task 5 - FILE HANDLING AND EXCEPTION HANDLING

#1.Write a program in Python to allow the error of syntax to be handled using exception handling.

###Answer: We cant handle syntax errors in python like other exceptions. Even if i use try and except
           #still seeing error while interpreting.
'''
try:
  print(-)
except:
  print("Syntax error occured")
  #raise Exception("Syntax error occured")
'''
#2.Write a program in Python to allow the user to open a file by using the argv module. If the
   #entered name is incorrect throw an exception and ask them to enter the name again. Make sure
   #to use read only mode.
'''
import sys
try:
  with open(sys.argv[1], 'r') as file:
    print(file.read())
except FileNotFoundError:
  print(input("It's incorrect file name, please enter file name again"))

#with open("try.txt","r") as file:
  #print(file.read())
'''
#3.Write a program to handle an error if the user entered a number more than four digits it should
   #return “The length is too short/long !!! Please provide only four digits” 
'''
Input_Data=input("Please enter the digits: ")
try:
  if len(Input_Data)<=4:
    print(Input_Data)
    print("Length of input is",len(Input_Data))
  elif len(Input_Data)>4:
    print("Length of input is",len(Input_Data))
    raise ValueError
except ValueError:
  print("The length is too short/long !!! Please provide only four digits")
'''
#4.Create a login page backend to ask users to enter the username and password. Make sure to
   #ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
   #should not be more than 3 times.
'''
count=0
while count<3:
    UserName=input('Enter username: ')
    Password=input('Enter password: ')
    if Password=='PrAnItHa' and UserName=='ConsultAdd':
        print("Login")
        break
    else:
        print("Incorrect Username or Password,Please Re-Type the UserName and Password")
        count+=1
print("Exceeded number of attempts")
'''
#5.Go through the link provided below to understand finally and raise concept:
 #   https://www.programiz.com/python-programming/exception-handling

#6.Read doc.txt file using Python File handling concept and return only the even length string from the file.
'''
with open("doc.txt","w") as file:
  file.write("Hello I am a file\n Where you need to return the data string\n Which is of even length\n Make sure you return the content in The same link as it is present")
with open("doc.txt") as file:
  contents = file.read()
  for i in contents.split(" "):
    if len(i)%2==0:
      print(i)
'''    
##TASK 6 - GENERATORS, LIST COMPREHENSION AND DECORATORS

#1.Write a program in Python to find out the character in a string which is uppercase using list comprehension
'''
String1="PraNItha"
Upper_Chars=[i for i in String1 if i.isupper()]
print(Upper_Chars)
'''
#2.Write a program to construct a dictionary from the two lists containing the names of students and
   #their corresponding subjects. The dictionary should map the students with their respective subjects.
   #Let’s see how to do this using for loops and dictionary comprehension.
   #HINT - Use Zip function also
'''
  #Using ZIP function
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict1=dict(zip(students,subjects))
print(dict1)
'''
'''
  #Using for loops
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict1={}
for key in students:
    for value in subjects:
        dict1[key]=value
        subjects.remove(value)
        break
print(dict1)
'''
'''
  #Using dictionary comprehension
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict1={students[i]:subjects[i] for i in range(len(students))}
print(dict1)
'''
#3.Learn More about Yield, next and Generators
#4.Write a program in Python using generators to reverse the string.
'''
def Str_Rev(String1):
    yield String1[::-1]
String1=Str_Rev("Consultadd Training")
for i in String1:
    print(i)
'''
'''
String1="Consultadd Training"
String2=String1[::-1]
print(String2)
'''
#5.Write an example on decorators.
'''
  # Using Decorator
def Division(num1,num2):
    result=num1/num2
    print(result)
def Swap_nums(func):
    def Swap(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return Swap
Division=Swap_nums(Division)
Division(2,4)
'''
'''
  #Using Regular function
def Division(num1,num2):
    if num1<num2:
        num1,num2=num2,num1
        result=num1/num2
        print(result)
    else:
        result=num1/num2
        print(result)
Division(4,2)
'''




