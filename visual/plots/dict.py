import matplotlib.pyplot as plt 
import random as rnd

def data():
  paths = {}
  print("What type of line you prefer ? (:,-- or -) ")
  line_preference = input()

  print("What colour do you like?(r, g or b)")
  colour_preference = input()
   
  print("What style of marker do you like? (o, s or ^)")
  marker_style = input()
  paths['line_style'] = line_preference
  paths['colour'] = colour_preference
  paths['marker_style'] = marker_style
  
  return paths

def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  
  for num_line in range(num_lines):
    values = data()
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
    plt.plot(x, y, format)
  
  plt.show()

def run():
  print("Running...")
  generate()
  print("Done!")
  
run()


