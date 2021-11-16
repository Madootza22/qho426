#Display message
print("\nProgram started!")

#Ask user to enter character
print("Please enter a standard character: ")
character = input()

if len(character) == 1:
  print("The ASCII code for {} is {}".format(character, ord(character)))
  print("The ASCII code for character is".format(character), ord(character))
else:
  print(("You should introduce just one character!"))
print()
print("\nProgram ended!")