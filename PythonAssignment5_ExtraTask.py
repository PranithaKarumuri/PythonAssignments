##Extra Task

#1.Create a list of given structure and get the Access list as provided below:
'''
Input_list=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Split_list=Input_list[5]
#print(Split_list)
list1=Split_list[0:4:]
print(list1)
list2=[Input_list[6],Input_list[7]]
print(list2)
list3=Input_list[0::2]
print(list3)
list4=Input_list[::-1]
print(list4)
last_split=Split_list[5]
list5=last_split[0]
print(list5)
del Input_list[0:]
print(Input_list)
'''
#2.Create a list of thousand numbers using range and xrange and see the difference between each other.
 #Answer: In python3 xrange() is renamed to range(). So there is no xrange() in python3.
'''
list1=[]
for i in range(1,1001):
    list1.insert(len(list1),i)
print(list1)
'''
#3.How Tuple is beneficial as compared to the list?
'''
# Answer: Tuples are more memory efficient than list and 
          when you data that shouln't change then better to use tuple than list.
'''
#4.Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
   #the number which is divisible by 3 and is a multiple of 2.
'''
list1=[]
for i in range(1,101):
    if i%3==0 and i%2==0:
        list1.insert(len(list1),i)
print(list1)
'''
#5.Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
   #string with their index.
'''
Str="Pranitha"
rev_str=Str[::-1]
print(rev_str)
vowels="a","e","i","o","u"
for i in Str:
    if i in vowels:
        print(i,"present at index",Str.index(i))
'''
#6.Write a program in Python to iterate through the string “hello my name is abcde” and print the
   #string which is having an even length.
'''
Str="hello my name is abcde"
words=Str.split(" ")
print(words)
for word in words:
    if len(word)%2==0:
        print(word)
'''
#7.Write a program in python to print the pair of numbers whose sum is equal to the result
   #number that is let's say 8.
'''
list1=[1,2,3,4,5,6,7,8,9,-1]
for i in range(0,len(list1)-1):
    for j in range(1,len(list1)):
        if (list1[i]+list1[j])==8:
            list2=[]
            #print(list1[i],list1[j])
            list2.insert(len(list2),[list1[i],list1[j]])
            print(list2)
'''
#8.Write a program in Python to complete the following task.
   #Create two lists such as even_list and odd_list
   #Ask user to enter a number in the range of 1,50 and make sure if the entered number is
    #even, append it to the even_list and if the entered number is odd append it to the odd_list.
   #Keep that in mind you can only add 5 items in each list
   #Make sure once you enter all the 5 elements, calculate the sum of the list and return the 
    #maximum of the list.
'''
even_list=[]
odd_list=[]
count=0
while count<5:
    number=int(input("Enter a number between 1 to 50: "))
    if number%2==0:
        even_list.append(number)
        print(even_list)
    elif number%2!=0:
        odd_list.append(number)
        print(odd_list)
        count+=1
print("Sum of numbers in even_list is: ",sum(even_list))
print("Sum of numbers in odd_list is: ",sum(odd_list))
print("maximum of numbers in even_list is: ",max(even_list))       
print("maximum of numbers in odd_list is: ",max(odd_list))
'''
#9.Write a program to find out the occurrence of a specific character from an alphanumeric string.
'''
Str="12abcbacbaba344ab"
print(Str)
for i in Str:
    if i.isalpha():
        chars=i
        print(chars,"occured for ",Str.count(chars),"times")
'''
#10.Generate and print another tuple whose values are even numbers in the given tuple.
'''
tup=(1,2,3,4,5,6,7,8,9,10)
tup1=list(tup)
tup2=[]
for i in tup1:
    if i%2==0:
        tup2.insert(len(tup2),i)
tup3=tuple(tup2)
print(tup3)
'''        
        






