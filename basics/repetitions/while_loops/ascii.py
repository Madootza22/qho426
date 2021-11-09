#Ask the user how many bars to be charged
print("\nHow many bars should be charged?")
bars_to_charge = int(input())

#Declare control variable
bars_charged = 0

#Bars charging
while (bars_charged < bars_to_charge):
  bars_charged = bars_charged + 1
  print("Charging: ", "|" * bars_charged)

print("\nThe battery is fully charged!")