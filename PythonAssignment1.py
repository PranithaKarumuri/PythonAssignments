##Task1 - Numbers and Variables

#1.Create three variables in a single line and assign values to them in such a manner that each one of
    #them belongs to a different data type.


'''
a,b,c=1,2.01,"string"
print(a)
print(b)
print(c)
'''

#2.Create a variable of type complex and swap it with another variable of type integer.
'''
x=5+3j
y=3
y=x
print(y)
'''
'''
x=5+3j
y=3
print(type(x))
print(type(y))
t=x
x=y
y=t
print(type(x))
print(type(y))
'''
'''
x=5+3j
print(x.real)
print(x.imag)
y=abs(x)
print(y)
print(type(y))
print(type(int(y)))
'''

#3.Swap two numbers using a third variable and do the same task without using any third variable.

#Swap two numbers using a third variable
'''
a=3
b=6
print(a)
print(b)
t=a
a=b
b=t
print(a)
print(b)

#Swaping two numbers without using third variable

x=2
y=4
print(x)
print(y)
x,y=y,x
print(x)
print(y)
'''

#4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

#Using Python2.x
'''
name=input("what is your name?")
print"name"
'''
#Using Python3.x
'''
name=input("what is your name? ")
print(name)
'''

#5.Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
   #another variable called z. Add 30 to z and store the output in variable result and print result as the
   #final output.

'''
x=input("Enter 1st number in between 1-10: ")
y=input("Enter 2nd number in between 1-10: ")
z=int(x)+int(y)
result=z+30
print(result)
'''

#6.Write a program to check the data type of the entered values.
    #HINT: Printed output should say - The data type of the input value is : int/float/string/etc

'''
x="Pranitha"
print("The data type of the input value is: ",type(x))
#y="The data type of the input value is: {}"
#print(y.format(type(x)))
'''

#7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

'''
#Upper CamelCase
CompanyName="ConsultAdd"
#Lower CamelCase
companyName="ConsultAdd"
#SnakeCase
company_name="ConsultAdd"
#UPPERCASE
COMPANYNAME="ConsultAdd"
'''

#8.If one data type value is assigned to 'a' variable and then a different data type value is assigned to 'a'
   #again. Will it change the value? If Yes then Why?
'''
Ans: Yes, value gets changed 
because the first time assigned value will get overlapped by the second time assigned value
'''
## Task2 - OPERATORS AND DECISION MAKING STATEMENT

#1.Write a program in Python to perform the following operation:
      #If a number is divisible by 3 it should print "Consultadd" as a string
      #If a number is divisible by 5 it should print "Python Training" as a string
      #If a number is divisible by both 3 and 5 it should print "Consultadd - Python Training" as a string.

'''
num=20
if num%3==0:
    print("Consultadd")
elif num%5==0:
    print("Python Training")
elif (num%3==0 and num%5==0):
    print("Consultadd - Python Training")
else:
    print("num is not divisible by either 3 or 5")
'''
#2.Write a program in Python to perform the following operator based task:
'''
print("Choose one from the following operation:\n1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n5 - Average")
Operation=input("Enter the desired operation number: ")
num1=int(input("Enter 1st number to perform operation: "))
num2=int(input("Enter 2nd number to perform operation: "))
if Operation=="1":
    Add=num1+num2
    print(Add)
    if Add<0:
        print("NEGATIVE")
elif Operation=="2":
    Sub=num1-num2
    print(Sub)
    if Sub<0:
        print("NEGATIVE")
elif Operation=="3":
    Div=num1//num2
    print(Div)
    if Div<0:
        print("NEGATIVE")
elif Operation=="4":
    Mul=num1*num2
    print(Mul)
    if Mul<0:
        print("NEGATIVE")
elif Operation=="5":
    num3=int(input("Enter number to perform average: "))
    num4=int(input("Enter another number to perform average: "))
    Avg=(num1+num2+num3+num4)/4
    print(Avg)
    if Avg<0:
        print("NEGATIVE")
'''
#3.Write a program in Python to implement the given flowchart:
'''
a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=",avg)
if avg>a and avg>b and avg>c:
    print("avg is higher than a,b,c")
elif avg>a and avg>b:
    print("avg is higher than a,b")
elif avg>a and avg>c:
    print("avg is higher than a,c")
elif avg>b and Avg>c:
    print("avg is higher than b,c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")
'''

#4.Write a program in Python to break and continue if the following cases occurs:
   #If user enters a negative number just break the loop and print “It's Over”
   #If user enters a positive number just continue in the loop and print “Good Going”

'''
num=int(input("Enter any number: "))
while num>=0:
    print("Good Going")
    continue
while num<0:
    print("It's Over")
    break
'''

#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
    #multiple of 5, between 2000 and 3200

'''
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i)
'''
#6.What is the output of the following code examples?

'''
x=123
for i in x:
    print(i)
'''
    #output: Error, as we cannot iterate integer
'''
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print("error")
'''
    #output: 0, error, 1, error, 2
'''
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break
'''
    #output: 0,1,2,3,4

#7.Write a program that prints all the numbers from 0 to 6 except 3 and 6 using continue statement.
'''
for i in range(0,6):
    if i==3 or i==6:
        continue
    print(i)
'''
#8.Write a program that accepts a string as an input from the user and calculate the number of digits and letters
'''
Str="Consul72"
alpha=0
for i in Str:
    if(i.isalpha()):
        alpha+=1
print("Number of digits are:",len(Str)-alpha)
print("Number of letters are:",alpha)
'''
#9.Read the two parts of the question below: 
'''
## Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
## Modify the program so that it asks users whether they want to guess again each time. Use two
variables, 'number' for the number and 'answer' for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number).
'''
 #Part a
'''
Lucky_Number=25
Guess_Number=int(input("Guess the lucky number: "))
while Lucky_Number==Guess_Number:
    print("You guessed correct number")
    break
while Lucky_Number!=Guess_Number:
    print("Guessed wrong number")
    continue
'''
 #Part b
'''
Lucky_Number=24
Answer=input("Do you want to guess the number: Yes or No ")
while Answer!="No":
    Number=int(input("Guess the lucky number: "))
    if Number==Lucky_Number:
        print("You guessed correct number")
    elif Number!=Lucky_Number:
        print("You guessed it wrong")
    Answer=input("Do you want to guess the number again: Yes or No ")
'''
#10.Write a program that asks five times to guess the lucky number. Use a while loop and a counter.
'''
Lucky_Number=24
counter=1
while counter<=5:
    Number=int(input(f"Guess the number {counter}: "))
    if Number==Lucky_Number:
        print("Good Guess")
    elif Number!=Lucky_Number:
        print("Try again")
    counter+=1
print("Game Over")
'''
#11.In the previous question, insert break after the “Good guess!” print statement. break will terminate
   #the while loop so that users do not have to continue guessing after they found the number. If the user
   #does not guess the number at all, print “Sorry but that was not very successful”
'''
Lucky_Number=24
counter=1
while counter<=5:
    Number=int(input(f"Guess the number {counter}: "))
    if Number==Lucky_Number:
        print("Good Guess!")
        break
    elif Number!=Lucky_Number:
        counter+=1
else:
    print("Sorry but that was not very successful") 
'''



        







 

        
   






    















