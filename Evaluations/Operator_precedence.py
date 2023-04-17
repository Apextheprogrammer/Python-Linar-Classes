a=int(input('Input value for a: '))
b=int(input('Input value for b: '))
c=int(input('Input value for c: '))
d=int(input('Input value for d: '))
e=int(input('Input value for e: '))
f=int(input('Input value for f: '))
sum=a+b
print('the sum of a and b is '+str(sum))
sub=c-d
print('the subtraction of c from d is '+str(sub))
multi=e*f
print('the multiplication e and f is '+str(multi))
div=f/e
print('the division of f by e is '+str(div))
mod=d%c
print('the modulus value for d modulus c is '+str(mod))
flrdiv=b//a
print('the floor division of b with a is '+str(flrdiv))
expo=a**f
print('the exponential of a to f is '+str(expo))
#Comparison operators
#greater than
print(2>1)
print(1>2)
#less than
print(5<7)
print(7<5)
#Equal to
print(5==4)
print(5==5)
#Not equal to
print(3!=4)
print(4!=4)
#greater than or equal
grt1=3>=4
print(grt1)
grt2=4>=4
print(grt2)
print('less than or equal')
print(5<=7)
print(7<=5)

#Logical operators
print('For AND')
and1=grt1 and grt1
print(and1)
and2=grt2 and grt1
print(and2)
print('For OR')
or1=grt2 or grt2
print(or1)
or2=grt1 or grt2
print(or2)
print('For NOT')
print(not div and multi)