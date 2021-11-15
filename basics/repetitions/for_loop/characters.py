#Ask the user to introduce markings
print("\nWhat strange markings do you see? ")
strange_markings = input()

#Identify the markings
print("\nIdentifying...")

for count in range(0, len(strange_markings), 1):
  print("index", count, ":", strange_markings[count])

print("\nDone!") 