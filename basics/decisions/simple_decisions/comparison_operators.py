#Ask user to enter the first number
print("Please enter the first number: ")
first = int(input())
 
#Ask user to enter the second number
print("Please enter the second number: ") 
second = int(input())

#Compare the two numbers and display message 
if first > second:
  print("\nThe second number is the smallest!")
elif second > first:
  print("\nThe first number is the smallest!")
else:
  print("\nBoth numbers are equal!")

