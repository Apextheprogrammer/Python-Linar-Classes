'''
a='Post Malone'
Sn,Fn=a.split(' ')

print(f'Mr {Sn}, Welcome here and Thanks.\nHey {Fn}, are you satisfied?\n'
 f'My greetings to the family of {Sn}\n\n ')

b='Ed Sheeran'
rn,dn=b.split(' ')

print(f'Mr {rn}, Welcome here and Thanks.\nHey {dn}, are you satisfied?\n'
 f'My greetings to the family of {rn}\n\n ')

c='Saint jhn'
Surname,First=c.split(' ')

print(f'Mr {Surname}, Welcome here and Thanks.\nHey {First}, are you satisfied?\n'
 f'My greetings to the family of {Surname} \n\n')

d='Post Malone'
last,Frst=d.split(' ')

print(f'Mr {last}, Welcome here and Thanks.\nHey {Frst}, are you satisfied?\n'
 f'My greetings to the family of {last} ')
'''



#names=['Post Malone','Saint jhn','Ed sheeran','De Bruyne','Loniel Messi']


'''
def take_name():
    entered_names=['dgr fes','re fw']
  
    #print(len(entered_names))
    if len(entered_names) == 2:
        for fullname in entered_names:    
            last, first = fullname.split(' ')
            print(f'Mr {last}, Welcome here and Thanks.\nHey {first}, are you satisfied?\nMy greetings to the family of {last}\n\n ')
    else:
        entered_names.append(input('Pls input your fullname: '))
        #take_name()
        '''

    
def take_name():
    ''''''
    entered_names=[]
    while len(entered_names) < 10:
        entered_names.append(input('Pls input your fullname: '))
    #print(len(entered_names))
    #if len(entered_names) == 2:
    for fullname in entered_names:    
        last, first = fullname.split(' ')
        print(f'Mr {last}, Welcome here and Thanks.\nHey {first}, are you satisfied?\nMy greetings to the family of {last}\n\n ')
    #else:
        
        #take_name()

#list_names.append(names)
#to_use = str(entered_names[0])


#ist_names.append()
#if len
take_name()















'''
a=10
a.as_integer_ratio

Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

>>> (10).as_integer_ratio()
(10, 1)
>>> (-10).as_integer_ratio()
(-10, 1)
>>> (0).as_integer_ratio()
(0, 1)

a.bit_count
a.bit_length

b=10.8
b.conjugate
b.as_integer_ratio
b.fromhex


def sum(n):
    s=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            s+=j #s=s+j
    return s

print(sum(3))

list=['ade']
list1=['ade','mike']
list2=['ade','mike',1]
list3=['dave','mike',1.2,'4']
list4=['eve','bike','help',10,'False']
list5=['David','Daniel','John','Cena','Falz','Strange'] #main stuff
list6=['go',1.11,'yellow','True',700,'None']

for name in list5:
    print(f'Good morning, {name}')
'''


