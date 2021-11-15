#Ask the user to introduce a number
print("\nHow far are we from the cave? ")
distance = int(input())

#Using a for loop to measure the distance in steps
for count in range(distance, 0, -1):
  print(count, "steps remaining")

print("\nWe have reached the cave! ")  
