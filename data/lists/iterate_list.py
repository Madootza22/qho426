def directions():
  directions = ["Move forward", "Move backward", "Turn left", "Turn right"]
  return directions
def menu():
  print("Please select a direction: ")
  dirs = directions()
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")

def run():
  menu()

run()      