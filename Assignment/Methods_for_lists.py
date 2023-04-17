list=['name',40,'good']

#clear
list.clear()#Used to clear the list, makes it empty
print(list)

#index
list=[40,40,1,2,3]#created a new listr, previous was cleared
print(list.index(3))#prints the index number of the argument put

#count
print(list.count(40))#prints the amount of appearances of the argument

#remove
list.remove(1)#remove method is used to remove objects in a list, in this case the object at index 0
print(list)#prints the result without the removed object

#sort
list.sort()
print(list)