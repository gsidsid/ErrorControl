import numpy as np
from scipy.linalg import solve
import sympy
import random
import binascii
import time


#Creating Hadamard Matrices
H2 = np.array([[1,1],
              [1,-1]])
H4 = np.kron(H2,H2)
H8 = np.kron(H4,H2)
# H16 = np.kron(H4,H4)

#Creating codeword matrix
C8 = np.concatenate((H8,-H8))
C8[C8 == -1] = 0

#All possible messages:
# messages = np.array([[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0],
#                       [0,0,1,1],[0,1,0,1],[0,1,1,0],[0,1,1,1],
#                       [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,1,0,0],
#                       [1,0,1,1],[1,1,0,1],[1,1,1,0],[1,1,1,1]])


# Creating Generator Matrix and row reduced version
G = np.array([[1,1,1,1,1,1,1,1],
            [0,0,0,0,1,1,1,1],
            [0,0,1,1,0,0,1,1],
            [0,1,0,1,0,1,0,1]])
reduced, _ = sympy.Matrix(G).rref()
# reduced = np.array(sympy.Matrix.tolist(reduced)).astype(np.float64)%2
Greduced = np.array([[1,0,0,1,0,1,1,0],
                      [0,1,0,1,0,1,0,1],
                      [0,0,1,1,0,0,1,1],
                      [0,0,0,0,1,1,1,1]])

# Parity check matrix
P = np.array([[1,1,1,1,0,0,0,0],
              [1,1,0,0,1,1,0,0],
              [1,0,1,0,1,0,1,0],
              [0,1,1,0,1,0,0,1]])
Pt = np.transpose(P)

#Check that all codewords are valid with parity check
# for message in messages:
#     codeword = np.dot(message,Greduced) % 2
#     print(codeword)
#     print(np.dot(codeword, Pt) % 2)


def getCodewords(inputchar):
    # Message
    #Ensures the message is length 8
    binary_m = format(ord(inputchar), 'b')
    if len(binary_m) < 8:
        pad = '0'
        binary_m = (8 - len(binary_m)) * pad + binary_m

    m = np.array([[0,0,0,0,0,0,0,0]])
    print('\n{}'.format(binary_m))
    for i in range(0,8):
        m[0][i] = binary_m[i]

    M = np.array([[0,0,0,0],[0,0,0,0]])
    M[0] = np.array(m[0][0:4])
    M[1] = np.array(m[0][4:8])
    # Codeword
    C1 = np.dot(M[0],Greduced) % 2
    C2 = np.dot(M[1],Greduced) % 2
    codes = [C1, C2]
    print('Original Codewords: {}'.format(codes))

    return codes


def noise(codeword, probability):
    R = codeword
    # Random Error Depending on probability
    error = []
    errorcount = 0
    for x in range(0,8):
        if random.random() < probability:
            error = error + [x]
            R[x] = (R[x] + 1) % 2
            errorcount += 1
    print('Noisy Message: {} Error: Positions {}'.format(R, error))
    return R


def mapToMessage(codeword):
    codeword = codeword.astype(np.int64)
    #Indices 1,2,3, and 5 make up the message
    message = np.array([0,0,0,0])
    #Grab first 4 bits from the codeword
    message += codeword[:4]
    #replace the 4th bit with the codeword's 5th bit
    message[3] = codeword[4]

    return message

def decode(received):
    #Recieved codeword
    R = received
    decoded = None

    ## Syndrome calculated with rHt
    Sv = np.dot(R, Pt) % 2

    #Create Syndrome/error vector finding array
    errorArray = np.zeros((8,8))
    syndromeArray = np.zeros((8,4))
    for i in range(8):
        errorArray[i][i] = 1
        syndromeArray[i] = np.dot(errorArray[i],Pt)

    errorVector = None

    if np.all(Sv==0):
        print('No errors detected')
        return(mapToMessage(R), "Not Corrected")
    else:
        for i in range(len(syndromeArray)):
            if np.array_equal(syndromeArray[i].flatten(), Sv.flatten()):
                errorVector = errorArray[i]
                print('Error detected in position {}'.format(i))
                return(mapToMessage((R - errorVector)%2),"Corrected")

    print("Detected 2 errors, could not correct")
    return (mapToMessage(R), "Not Corrected")


def translate(decodemsgs):
    binstr = ''.join(str(x) for x in decodemsgs[0])
    binstr = binstr + ''.join(str(x) for x in decodemsgs[1])
    translatedcode = chr(int(binstr,2))

    return translatedcode

def processMessage(message, probability):
    print('Encoding and Decoding "{}"'.format(message))
    decodemessage = ''
    correctedIndices = []
    for index, letter in enumerate(message):
        A = getCodewords(letter)
        code1 = noise(A[0], probability)
        code2 = noise(A[1], probability)
        print(code1, code2)
        messagePart1, ifCorrected1 = decode(code1)
        messagePart2, ifCorrected2 = decode(code2)
        if (ifCorrected1 == "Corrected") or (ifCorrected2 == "Corrected"):
            correctedIndices.append(index)
        result = translate([messagePart1, messagePart2])
        decodemessage += result
    print('\nYour message was {0}'.format(decodemessage))
    return (decodemessage, correctedIndices)

def hadamardDecoding(message, probability):
    decodedMessage, correctedIndices = processMessage(message, probability)
    errorLocs = []
    for i in range(len(message)):
        if message[i] != decodedMessage[i]:
            errorLocs.append(i)
    return [decodedMessage, errorLocs, correctedIndices]

# print(hadamardDecoding("01234567", .05))
