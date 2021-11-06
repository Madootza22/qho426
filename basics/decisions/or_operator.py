#Ask user the type of adventure
print("\nWhat type of adventure should I have?") 
adventure_type = input()

#Determine the message to display
if ( (adventure_type == "scary") or (adventure_type == "short") ):
  print("\nEntering the dark forest!")
elif ( (adventure_type == "safe") or (adventure_type == "long") ):
  print("Taking the safe route!")
else:
  print("Not sure which route to take!")
     