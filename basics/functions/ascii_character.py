#display message
print("Program Started!")
#Ask user to introduce an ASCII code
print("Please enter an ASCII code:")
code = int(input())

if (code >= 32 and code <= 126):
  print("The character represented by the ASCII code {} is {} ".format(code, chr(code)))
  print("The character represented by the ASCII code is ".format(code), chr(code))
else:
  print("The character cannot be displayed.")

print("Program Ended!")