#Define functions
def climb_ladder(remained_steps, steps_crossed):
  if remained_steps > steps_crossed:
    print("Still some way to go!")
  else:
    print("We are almost there!") 

#Call the functions
climb_ladder(5, 2)  
climb_ladder(2, 5)   