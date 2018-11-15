
food1 = input("Input food 1: ")
food2 = input("Input food 2: ")
food3 = input("Input food 3: ")

foods = [food1, food2, food3]

foods.sort()
print(foods)


a = 4 #Create a variable called a and store 4 in it

#Lists has a legth of 6 and indexes 0 - 5
#	    0 1 2 3 4 5
list = [1,2,3,4,5,6]

#To access the data in the list we need the list name and the index

print (a)
print (list)

print (list[0]) #List at index 0
print (list[1]) #list at index 1
print (list[5]) #List at index 5 

lenList = len(list)
print (list[lenList-1])

list[0] = 999
print (list)

list[lenList-1] = 9999
print (list)

#The append list.append command adds the sugested feature to the
#end of your list
list.append(76)
print (list)