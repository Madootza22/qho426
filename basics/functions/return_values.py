#Define functions
def sum_weights(Bop_weight, Beep_weight):
  total_weight = Bop_weight + Beep_weight
  return total_weight

def calc_avg_weight(Bop_weight, Beep_weight):
  avg_weight = (Bop_weight + Beep_weight) / 2
  return avg_weight

def run():
  print("What is the weight of Bop?")
  Bop_weight = float(input())

  print("What is the weight for Beep?")
  Beep_weight = float(input())

  print("What do you want to calculate? (sum/average)")
  action = input()

  if action == "sum":
    answer = sum_weights(Beep_weight, Bop_weight)
    print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
  elif (action == "average"):
    answer = calc_avg_weight(Beep_weight, Bop_weight)
    print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
  else:
        print("I am not sure what you would like to do.")

#Run the program
run()