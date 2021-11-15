#Ask user to introduce number of rows
print("\nHow many rows should I have? ")
rows = int(input())

#Ask user to introduce number of columns
print("\nHow many columns should I have? ")
columns  = int(input())

#Create nested loop
for row in range(0, rows, 1):
  for column in range(0, columns, 1):
    print(":-)", end="")
  print()    
print()
print("Done! ") 