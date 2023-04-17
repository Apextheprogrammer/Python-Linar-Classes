'''
print('Hey there!.... Give us numbers and watch is add them all together!')
first=int(input('Enter a number: '))
second=int(input('Enter a number: '))
third=int(input('Enter a number: '))
fourth=int(input('Enter a number: '))
fifth=int(input('Enter a number: '))
x=[first,second,third,fourth,fifth]

def av():
    s=0
    for num in x:
        s+=num
        result=s/5
    return result
print(f'Answer is {av()}')

a=range(2,100000000,2) #Range for even numbers
x=int(input('Enter number: '))
if x in a:
    print('Even')
else:
    print('Odd')
    '''


print('Hello there!....Lets do a quick calculation.\nNOTE: Any number given will be multiplied by 10') #Greetings
number=float(input('Enter number: '))
def mul():
    '''Divides input by 10'''
    result=number*10 #variable for the result
    return result
print(f'Your answer is {mul()}') #prints the result