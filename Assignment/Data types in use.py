print('This is a test Addition Calculator designed by APEX tech.') #just an intro
print('Lets start with whole numbers shall we? ')#this one no necessary but we move
first_number=int(input('What is your first number? ')) #collect the number and turn the input to an interger
second_number=int(input('What is your second number?'))#collect the number and turn the input to an interger
ans1=print('The solution is '+ str(first_number + second_number))#add the two numbers

print('Nice it works! Now we move to decimals.')#cringe
first_decnumber=float(input('What is your first number? ')) #collect the number and turn the input to an interger
second_decnumber=float(input('What is your second number?'))#collect the number and turn the input to an interger
ans2=print('The solution is '+ str(first_decnumber + second_decnumber))#add the two decimal numbers, turned the answer to a string
check1=type(first_number)#creating a variable for the type of data type
print(check1)#checking if the first input was an interger
check2=type(second_decnumber)#creating a variable for the type of data type
print(check2)#checking if the second input was an float