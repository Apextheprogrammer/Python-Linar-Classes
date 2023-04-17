def div(a,b,c):
    divide=a/b+c
    print(divide)
div(4,2,3)
def greetings(name,department):
    hello=f'Good morning {name}, Welcome to {department}. '
    print(hello)
greetings('David','python')
def absestors(length1,breadth1,length2,breadth2):
    No_of_absestors= (length1*breadth1)/(length2*breadth2)
    print(f'The total number of absestors needed are {No_of_absestors}')
absestors(12,12,4,4)
def footy(player,position):
    print(f'Youre {player},  and your preffered position is {position}')
footy('Messi','Central Midfield')
def records(player,record):
   print(f'{player} has the {record}.')
records('Haaland','Highest number of goals')
def scores(score1,score2,score3,score4):
    avgscore=(score1+score2+score3+score4)/4
    print(avgscore)
scores(1,2,3,4)
def vehicle(weight,tyres):
    print(f'if Your vehicle weighs between {weight} , it will have {tyres} tyres')
vehicle('10kg to 100kg',2)
vehicle('101kg to 150kg',3)   
vehicle('151kg to 800kg',4)
def sum(a,b,c,d):
    addition=a+b+c+d
    print(f'The summation of the numbers is {addition}')
sum(3,4,5,6)
def welcome(greetings,name,age,course,place):
    print(f'{greetings} {name}, you are {age} old. The course you are about learning is {course} and will be taken in {place}.')
welcome('Good evening','David','18yrs', 'python','Linar')
def welcome(greetings,name,age,course,place):
    print(f'{greetings} {name}, you are {age} old. The course you are about learning is {course} and will be taken in {place}.')
welcome('Good afternoon','Apex','20yrs', 'C++','Linar')
def exam(name,subject,obj,theory):
    resultper=((obj+theory)/70)*100
    print(f'Good day {name}, you scored {int(resultper)}% in your just concluded {subject} exam.' )
exam('David','Chemistry',20,45)
def exam(name,subject,obj,theory):
    resultper=((obj+theory)/70)*100
    print(f'Good day {name}, you scored {int(resultper)}% in your just concluded {subject} exam.' )
exam('Apex','Physics',20,50)