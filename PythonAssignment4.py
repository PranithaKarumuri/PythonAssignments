##Task - 7 CLASSES AND OBJECTS

#1. Write a program that calculates and prints the value according to the given formula:
'''
import math
C=50
H=30
list1=input("Enter the values for D: ")
list1=list1.split(",")
list2=[]
for D in list1:
    Q=round(math.sqrt((2*C*int(D)/H)))
    list2.append(Q)
print(list2)
'''
#2.Define a class named Shape and its subclass Square. The Square class has an init function which
   #takes length as argument. Both classes have an area function which can print the area of the shape
   #where Shape’s area is 0 by default.
'''
class Shape():
    #def __init__(self):
        #pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        #Shape.__init__(self) 
        self.length = length
    def area(self):
        return self.length*self.length
Square= Square(5)
print(Square.area())
'''
#3.Create a class to find three elements that sum to zero from a set of n real numbers
'''
def Sum_Zero(list1, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (list1[i] + list1[j] + list1[k] == 0):
                    #print(list1[i], list1[j], list1[k])
                    list2=[]
                    list2.insert(len(list2),[list1[i],list1[j],list1[k]])
                    print(list2)
                    found = True
    if (found == False):
        print(" Sum of three numbers to zero doesnot exist in list ")
list1 = [-25,-10,-7,-3,2,4,8,10]
n = len(list1)
Sum_Zero(list1, n)
'''
#4.Create a Time class and initialize it with hours and minutes.
   #Create a method addTime which should take two Time objects and add them.
   #Create another method displayTime which should print the time.
   #Also create a method displayMinute which should display the total minutes in the Time.
'''
class Time():
    def __init__(self, hours, mins):
	    self.hours = hours
	    self.mins = mins
    def addTime(t1, t2):
	    t3 = Time(0,0)
	    if t1.mins+t2.mins > 60:
		    t3.hours = (t1.mins+t2.mins)/60
	    t3.hours = t3.hours+t1.hours+t2.hours
	    t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
	    return t3
    def displayTime(self):
	    print ("Time is",int(self.hours),"hours and",int(self.mins),"minutes.")
    def displayMinute(self):
	    print (int(self.hours*60+self.mins),"minutes")

t1 = Time(2,50)
t2 = Time(1,20)
c = Time.addTime(t1,t2)
c.displayTime()
c.displayMinute()
'''
#5.Write a Person class with an instance variable “age” and a constructor that takes an integer as a
   #parameter. The constructor must assign the integer value to the age variable after confirming the
   #argument passed is not negative; if a negative argument is passed then the constructor should set
   #age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:
   ##yearPasses() should increase age by the integer value that you are passing inside the function.
   ##amIOld() should perform the following conditional actions:
     ###f age is between 0 and <13, print “You are young”.
     ###If age is >=13 and <=19 , print “You are a teenager”.
     ###Otherwise, print “You are old"
'''
class Person:
    def __init__(self,age):
        if age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = age
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif self.age>=13 and self.age<=19:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 12
        print(self.age)
age=int(input("Enter the age: "))
msg=Person(age)
msg.amIOld()
msg.yearPasses()
msg.amIOld
'''  




    




  





