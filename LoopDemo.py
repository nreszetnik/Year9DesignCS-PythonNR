#A loop structure is a structure that allows us to 
#run a section of code a number of times. It is great 
#for when we need to repeat a process. It is also great 
#when we need to run a pattern

# There ar two broad categories loops
# Conditional Loop: This loops as long as something is true 
# Counted Loop: This loops a set number o times

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("*******************************")
#The general structure of ac counted loop is 
#Count: This is the variable we use to track the number of
#times a loop runs
#Check: This the boolean (true or false) statemnet we evaluate 
# to decide if we keep goung
#Change: This is the change in the count that happens after each loop.each


#We use i in range loop
for i in range(0, 6, 1):
	print(i)

#How would the above loop run
# we would reach line 27
# i = 0, 0 < 6, True RUN LOOP
# i = 1, 1 < 6, True RUN LOOP
# i = 2, 2 < 6, True RUN LOOP
# i = 3, 3 < 6, True RUN LOOP
# i = 4, 4 < 6, True RUN LOOP
# i = 5, 5 < 6, True RYN LOOP
# i = 6, 6 < 6, False EXIT LOOP AND MOVE ON

print("*******************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)
print("*******************")
print("Write a loop that will print out even numbers from -22 to 134 inclusive")
for i in range(-22, 135, 2):
	print(i)

print("*******************")
print("We can count backwards as well. Python3 will assume the check based on")
print("relative value of the count and the check")

for i in range(3,0,-1):
	print(i)

print("*******************")
print("Print out all number from 101 to 0 inclusive")

for i in range(101, -1, -1):
	print(i)

print("**************")
print("Print all numbers from 1 to 8 inclusive")

s = "Fish Food"
#Never type in length of string as a
#number. Always have the computer find it
for i in range(0,len(s), 1):
 	print(s[i])

print("************************")

for i in range(8,-1,-1):
	print(s[i])

print("*******************")

for i in range(0, len(s), 2):
	print(s[i])




