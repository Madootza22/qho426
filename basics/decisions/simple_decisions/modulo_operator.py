#Ask user to enter a whole number
print("\nPlease enter a whole number: ")
number = int(input())

#Display message to tell the user if number is even or odd
if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
else:
    print("\nThe number {} is an odd number.".format(number))
