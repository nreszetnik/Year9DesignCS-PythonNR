
#opens up my file commGold.txt and 
#prepars it to be read. 
f = open("commGold.txt","r")
print(f.readline())
print(f.readline())

str = f.readline()
locStar = str.index("*")
print(locStar)

print(str[locStar+1]