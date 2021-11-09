#Ask user to enter favourite type of movie
print("\nWhat is your favourite type of movie? ")
movie = input()

#Display appropriate message depending on movie type
if movie == "comedy" or movie == "cartoon":
  print("Do you enjoy to laugh?")
  enjoy = input()
  if enjoy == "yes":
    print("Have a good time watching it!")
  if enjoy == "no":
    print("\nSometimes I don't like to laugh! ")  
  else:
    print("You should try another type of movie!")
elif movie == "action" :
  print("\nDo you enjoy action in movies?")
  action = input()
  if action == "yes":
    print("\nYou made a good choice! ")
  if action == "no":
    print("\nIt's totally fine! ")   
else:
  print("\nIt's enterely up to you what you want to choose!")       