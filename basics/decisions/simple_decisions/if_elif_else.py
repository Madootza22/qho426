#Ask user wich direction to paint
print("\nTowards which direction should i paint? ")
direction = input()

#Determine which is the direction of painting and print the correspondent message
if (direction == "up"):
  print("\nI am painting in the upward direction")
elif (direction == "down"):
  print("\nI am painting in the downward direction")
elif (direction == "left"):
  print("\nI am painting in the leftward direction")
elif (direction == "right"):
  print("\nI am painting in the rightward direction")
else:
  print("\nNot sure which direction I am painting in!")      
  