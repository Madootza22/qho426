#Ask user to introduce phrase
print("\nWhat phrase do you see?")
phrase = input()

#Reversing the phrase
print("\nReversing...\nThe phrase is ", end="")

for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")