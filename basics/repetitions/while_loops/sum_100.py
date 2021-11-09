#Display start message
print("\nCalculating the sum of the first 100 numbers...")

#Declare a control variable
number = 1

#Calculating sum from 1 to 100 inclusive
total = 0
while (number <= 100):
  total = total + number
  number = number + 1

#Display the result
print("...Done! The answer is ", total)  