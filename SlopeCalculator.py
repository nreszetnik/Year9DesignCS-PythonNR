import os
print ("Slope Calculator88888:")
os.system("say Welcome to my slope calculator")
#Input
x1 = input("Input x1: ")
x1 = int(x1)

y1 = input("Input y1: ")
y1 = int(y1)

x2 = input("Input x2: ")
x2 = int(x2)

y2 = input("Input y2: ")
y2 = int(y2)

#Process
rise = x2 - x1
run = y2 - y1

fSlope = rise/run

#Output
print("Your slope is m ="+str(rise)+"/"+str(run))
print("Your slope as a decimal is ",fSlope)
os.system("say Your slope as a decimal is "+str(fSlope))
print(rise)
print(run)