#A list of values
goldValue = [123,124,125]

money = float(input("How much money do you have? "))

print("What buying option do you want")
print("1. Highest Value")
print("2. Lowest Value ")
print("3. Average")
choice = int(input("Input: "))

#How do I find the average of a list of numbers
total = 0

for i in range(0,len(goldValue),1):
	total = total + goldValue[i]

average = total/len(goldValue)

print("Your total buying power is based on average cost")
totalBuyingPower = money/average
print(totalBuyingPower)