name=input('Enter your name: ')
current_level=int(input('Enter your current level: Level '))
#current_salary is N30k

if 1<=current_level<=10:
    print('Welcome '+name)
    search_level=int(input('What level are you looking for? Level '))
else:
     print('This level does not exist. ')
   
a=30000
"""Level 1 salary"""
r=1.1 
"""Common ratio"""
search_level_salary=a*r**(search_level-1)
if 1<=search_level<5: #Lower class
    print('The class is lower class level '+ str(search_level)+ ' and salary for this level is N'+ str(int(search_level_salary)))#putting int so the value wont be in Decimals
elif search_level==5:#Middle class
    print('The class is Middle class level '+ str(search_level)+ ' and salary for this level is N'+ str(int(search_level_salary)))
elif 6<=search_level<=10:#Upper class
    print('The class is Upper class level '+ str(search_level)+ ' and salary for this level is N'+ str(int(search_level_salary))) 
else:
    print('Levels beyond 10 do not exist on our database.')