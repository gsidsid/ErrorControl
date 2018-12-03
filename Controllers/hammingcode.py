import numpy as np
import random
import binascii

def getCodewords(inputchar):
    # Generator Matrix
    G = np.array([[1,0,0,0,1,1,1],
        [0,1,0,0,1,0,1],
        [0,0,1,0,1,1,0],
        [0,0,0,1,0,1,1]])

    # Message
    binary_m = format(ord(inputchar), 'b')
    m = np.array([[0,0,0,0,0,0,0,0]])
    print(binary_m)
    for i in range(0,7):
        m[0][i] = binary_m[i]
    print(m)
    M = np.array([[0,0,0,0],[0,0,0,0]])
    print(m[0][4:8])
    M[0] = np.array(m[0][0:4])
    M[1] = np.array(m[0][4:8])
    print(M)
    # Codeword
    C1 = np.dot(M[0],G) % 2
    C2 = np.dot(M[1],G) % 2
    print('Original Codewords:')
    print(C1, C2)

    return (C1, C2)

def noise(codewords):
    # Random Error
    error = random.randint(0,6)
    # print(R[0][error], error)
    R[0][error] = (R[0][error] + 1) % 2
    print(R[0][error], error)
    print(R)

def decode(received):
    H = np.array([[1,1,1,0,1,0,0],
        [1,0,1,1,0,1,0],
        [1,1,0,1,0,0,1]])

    Ht = np.transpose(H)

    # Syndromes Calculated with Venn Diagram Equations
    S1 = R[0][0] + R[0][1] + R[0][2] + R[0][4]
    S2 = R[0][0] + R[0][2] + R[0][3] + R[0][5]
    S3 = R[0][0] + R[0][1] + R[0][3] + R[0][6]
    S1 = S1 % 2
    S2 = S2 % 2
    S3 = S3 % 2
    S = [[S1, S2, S3]]

    # Syndrome calculated with rHt
    Sv = np.dot(R, Ht) % 2

    # Find matching column index in parity matrix
    for i in range(0,6):
        if np.all(Ht[i][:]==Sv[0]): # rHt syndrome
            print(Ht[i], i)
            elocation = i
        else:
            continue
    # for i in range(0,6):
    #     if np.all(Ht[i][:]==S[0]): # Equations syndrome
    #         print(Ht[i], i)
    #     else:
    #         continue

    # correcting error
    R[0][elocation] = (R[0][elocation] + 1) % 2
    print(R)

    decoded = R[0][:4] # message is first four bits
    print(decoded)

getCodewords('h')
