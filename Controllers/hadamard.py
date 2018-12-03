import numpy as np
from scipy.linalg import solve
import random
import binascii
import time


#Creating Hadamard Matrices
H2 = np.array([[1,1],
              [1,-1]])
H4 = np.kron(H2,H2)
H8 = np.kron(H4,H2)
H16 = np.kron(H4,H4)
H128 = np.kron(H16,H8)


#How to make -1 into zeroes
z = np.array([[1, 1, -1, 1],
            [1, 1, -1, 1]])
z[z == -1] = 0
# print(z)

#Creating codeword matrix, has 256 rows
C128 = np.concatenate((H128,-H128))


# noise_prob = 0.05
#
# def decision(probability):
#     return random.random() < probability
#
# print(" ")
# toControlMessage = input("Enter a message: \n")
# binarizedMessage = ' '.join(format(ord(x), '08b') for x in toControlMessage)
# print("")
# print("Converted to binary: ")
# print("---------------------------------------")
# print(binarizedMessage)
# print("")
# binarizedLetters = [format(ord(x), 'b') for x in toControlMessage]
# parities = []
#
# for letter in binarizedLetters:
#     parity = 0
#     i = 0
#     for bit in letter:
#         val = int(bit)
#         if val == 1:
#             i+=1
#     if i % 2 != 0:
#         parity = 1
#     parities.append(parity)
#
# print("")
# print("Calculated parities: ")
# print("---------------------------------------")
# print(parities)
# print("")
#
# print("")
# print("Appending parities. This will make the number of ones in each bitstring even.")
# print("---------------------------------------")
# binarizedLettersWithParityBits = []
# for j in range(len(binarizedLetters)):
#     binarizedLettersWithParityBits.append(binarizedLetters[j] + str(parities[j]))
# print(binarizedLettersWithParityBits)
# print("")
#
# print("")
# print("Jamming...")
# print("---------------------------------------")
# jammed = []
# for letter in binarizedLettersWithParityBits:
#     if decision(noise_prob):
#         print("Jam!")
#         controlledMessage = letter
#         to_switch = random.randint(0,len(controlledMessage)-1)
#         if (controlledMessage[to_switch] == '1'):
#             new = list(controlledMessage)
#             new[to_switch] = '0'
#             jammed.append(''.join(new))
#         elif (controlledMessage[to_switch] == '0'):
#             new = list(controlledMessage)
#             new[to_switch] = '1'
#             jammed.append(''.join(new))
#     else:
#         jammed.append(letter)
# print(jammed)
# print("")
#
# print("")
# print("Decoding...")
# print("---------------------------------------")
# decoded = []
# new_parities = []
#
# for letter in jammed:
#     new_parities.append(int(letter[-1]))
#     decoded.append(letter[0:-1])
#
# print(decoded)
# print("")
#
# print("")
# print("Message received!")
# print("---------------------------------------")
# final = []
# ret = ""
# for message in decoded:
#     let = (chr(int(message, 2)))
#     final.append(let)
#     ret = ''.join(final)
#
# # wait 10 ms for every bit in the codeword (80 ms/byte)
# time.sleep((len(''.join(decoded))*10)/1000)
# print(ret)
# print("")
#
# print("")
# print("Error detection:")
# print("---------------------------------------")
# errs = []
# j = 0
# for message in decoded:
#     i = 0
#     for bit in message:
#         val = int(bit)
#         if val == 1:
#             i+=1
#     if i%2 == 0 and new_parities[j] == 0:
#         errs.append(False)
#     elif i%2 == 1 and new_parities[j] == 1:
#         errs.append(False)
#     else:
#         errs.append(True)
#     j+=1
#
# errors_detected_idx = [i for i, x in enumerate(errs) if x]
# for e_id in errors_detected_idx:
#     print("ERROR: " + final[e_id])
