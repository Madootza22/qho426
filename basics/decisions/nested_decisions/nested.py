#Ask the user to enter the cover type of the book
print("\nPlease enter the cover type of the book(hard/soft): ")
cover_type = input()

#Display appropriate message
if (cover_type ==  "soft"):
  print("Is is perfect bound?")
  perfect_bound = input()
  if perfect_bound == "yes":
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books.") 
else:
  print("Books with hard covers can be more expensive.")     


