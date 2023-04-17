#1) Variable Data Types
#a) Create a variable called "age" and assign it the value 25. Print the value of the variable.
#b) What is the difference between an integer and a floating-point number in Python? Provide an example for each.

#a
age=25
print(age)

#b

#An interger is a whole number without any decimal points(eg 1,2,3....) while a floating point number is a number 
#that contains a decimal point in it(eg 1.0,2.1,3.2.....)


#2) Basic Operations
#a) Write a Python program that adds two numbers together and prints the result.
#b) Write a Python program that takes a number as input and multiplies it by 10. Print the result.

#a
print('Hello there!....lets help you add some numbers') #Greetings
first_number=float(input('What is your first number: ')) #User inputs first number
second_number=float(input('What is your first number: ')) #User inputs second number

def add():
    '''this funtion adds two numbers together'''
    sum=first_number+second_number #adds the two inputs in the variables
    return sum
print(f'Your answer is {add()}') #prints the result

#b

print('Hello there!....Lets do a quick calculation.\nNOTE: Any number given will be multiplied by 10') #Greetings
number=float(input('Enter number: '))
def mul():
    '''Divides input by 10'''
    result=number*10 #variable for the result
    return result
print(f'Your answer is {mul()}') #prints the result

#3) Control Structures
#a) Write a Python program that checks if a number is even or odd. If the number is even, print "Even", otherwise print "Odd".
#b) Write a Python program that takes a number as input and checks if it is positive, negative, or zero. Print the result.

#a
a=range(2,100000000,2) #Range for even numbers
x=int(input('Enter number: '))
if x in a:
    print('Even')
else:
    print('Odd')

#b
numbr=input('Enter number: ')
if numbr=='0': 
    print('Input was 0')
elif numbr.startswith('-')==True:
    print('Negative number')
elif numbr.startswith('+')==True:
    print('Positive number')
elif numbr.startswith('')==True:
    print('Positive number')
else:
    print('input numbers only.')





#4) Lists and Loops
#a) Create a list of numbers from 1 to 10. Print each number in the list using a loop.
#b) Write a Python program that takes a list of numbers as input and returns the sum of all the numbers in the list.

#a
list=[1,2,3,4,5,6,7,8,9,10] #A list from 1 to 10
for x in list: #to iterate between the numbers
    print(x)

#b
print('Hey there!.... Give us numbers and watch is add them all together!')
a=int(input('Enter a number: '))
b=int(input('Enter a number: '))
c=int(input('Enter a number: '))
d=int(input('Enter a number: '))
e=int(input('Enter a number: '))
x=[a,b,c,d,e]

def num():
    '''Used to iterate between the numbers given and adds them together'''
    s=0
    for num in x:
        s+=num #s=s+num
    return s
print(f'Answer is {num()}')



#5) Functions
#a) Write a Python function that takes two numbers as input and returns their sum.
#b) Write a Python function that takes a list of numbers as input and returns the average of all the numbers in the list.

#a
def sum():
    '''Adds two numbers together'''
    a=float(input('Enter first number: '))
    b=float(input('Enter second number: '))
    result=a+b
    print(f'Answer is {result}')#prints result
sum() #Calling the function

#b
print('Hey there!.... Give us numbers and watch us add them all together and give you the average!')
first=int(input('Enter a number: '))
second=int(input('Enter a number: '))
third=int(input('Enter a number: '))
fourth=int(input('Enter a number: '))
fifth=int(input('Enter a number: '))
x=[first,second,third,fourth,fifth] #Create a list fro the inputs

def av():
    '''Function gives the average of the inputs'''
    s=0
    for num in x:
        s+=num
        result=s/5
    return result
print(f'Answer is {av()}')





#6) File Handling
#a) Write a Python program that reads a text file and prints its contents to the console.
#b) Write a Python program that writes a list of numbers to a text file.

#a
with open('text_file.txt','r') as file:
    content=file.read()
    print(content)

#b
with open('new_text.txt','w') as doc:
    input=doc.write('1,2,3,4,5,6,7,8,9,10')

#7) Libraries and Modules
#a) Install and Import the "math" module and use its "sqrt" function to calculate the square root of a number.
#b) Install and Import the "random" module and use its "randint" function to generate a random number between 1 and 10.
#c) Install and Import the "pywhatkit" module and use its "whatsapp" function to send a DM to your tutor with the body “Good Day Sir”

#a
import math as mt
number=float(input('Input number: '))
print(mt.sqrt(number))

#b
import random as ran
print(ran.randint(1,10))

#c
import pywhatkit as pyw
pyw.sendwhatmsg_instantly('+2349023459712','Good Day Sir',15,False)

#10) Give a feedback on this Python course, your instructor and this examination.

#Its been a really good course and was totally worth the time, energy and money. Learnt a lot in a space of few weeks and 
#I can proudly say i am a pythonista.

#On the instructor, Hes really good at teaching and he has the perfect blend between strict and friendly which is necessary
#For optimal learning..... hes definitely top notch.

#On this examination? Well i havent done much pressure thinking in a while.... i feel so alive and the questions are very solid python questions
#as they touch almost all the topics.