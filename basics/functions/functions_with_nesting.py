#Define functions and ask user
def identify():
  print("What do you see in front of us?")
  response = input()
  if response == "a large boulder":
    print("It's time to run!")
  else:
    print("We will be fine!") 

#Call the function
identify()     