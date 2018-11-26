import numpy as np
from scipy.linalg import solve

print(" ")
toControlMessage = raw_input("Enter a message: \n")
binarizedMessage = ' '.join(format(ord(x), 'b') for x in toControlMessage)
print("")
print("Converted to binary: ")
print("---------------------------------------")
print(binarizedMessage)
print("")
binarizedLetters = [format(ord(x), 'b') for x in toControlMessage]
parities = []

for letter in binarizedLetters:
    parity = 0
    i = 0
    for bit in letter:
        val = int(bit)
        if val == 1:
            i+=1
    if i % 2 != 0:
        parity = 1
    parities.append(parity)

print("")
print("Calculated parities: ")
print("---------------------------------------")
print(parities)
print("")

print("")
print("Appending parities. This will make the number of ones in each bitstring even.")
print("---------------------------------------")
binarizedLettersWithParityBits = []
for j in range(len(binarizedLetters)):
    binarizedLettersWithParityBits.append(binarizedLetters[j] + str(parities[j]))
print(binarizedLettersWithParityBits)
print("")