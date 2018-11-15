import math 
x = float(input ("Input one leg of the triangle: "))
y = float(input ("Input one leg of the traingle: "))

#Step One: Square X
x = x * x
#Step Two: Squre Y
y = y * y
#Step Three: add x and y and store in a temp variable
temp  = x + y
#Step Four: Take square root of temp
r = math.sqrt(temp)

print("A right triangle with side lengths",x,',',y,"will have a hypotenuse of ",r)
