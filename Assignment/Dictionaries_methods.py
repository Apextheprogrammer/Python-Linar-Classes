#COPY METHOD
original_thisdict={'brand': 'Toyota','currency': 'dollar','pair':'EURJPY'}#original dictionary
copied_thisdict=original_thisdict.copy() #copied dictionary
original_thisdict['brand']='Benz'#changed the value in the brand key to Benz
print(original_thisdict)#the value is changed when printed
print(copied_thisdict)#the value for the orginal is not changed here for the copy version when printed

#CLEAR METHOD
original_thisdict.clear()#this clears the intial keys and values within the dic
print(original_thisdict)#prints empty dic cause it has been cleared
original_thisdict={'car':'benz', 'country':'Spain'}#inputting new values to the cleared dic
print(original_thisdict)

#ITEMS
print(original_thisdict.items())#prints the items in the dic

#POP
popped_original_thisdict=original_thisdict.pop('car')#created a variable for the popped value
print(popped_original_thisdict)#prints the popped value
print(original_thisdict)#when printed, the popped key is removed from the dic

#FROMKEYS
first_names=['David','Apex','Josh']#list of names
ages=[40]#a list for an interger
new_dic=dict.fromkeys(first_names,ages)#merging the two to create a dic
print(new_dic)#dic is printed

original_thisdict.