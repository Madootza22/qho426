#Define function
def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  #return min(likelihoods)
  return max(likelihoods)

def run():
  #print(f"Minimum likelihood of falling: {likelihood()}%")
  print(f"Maximum likelihood of falling: {likelihood()}%")

run()    