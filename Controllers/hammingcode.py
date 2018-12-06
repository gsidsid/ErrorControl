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
    C1 = np.dot(M[0],G) % 2
    C2 = np.dot(M[1],G) % 2
    codes = [C1, C2]
    print('Original Codewords: {}'.format(codes))
    
    return codes

def noise(codeword):
    R = codeword
    # Random Error
    error = random.randint(0,6)
    R[error] = (R[error] + 1) % 2
    print('Noisy Message: {} Error: Position {}'.format(R, error))
    return R

def decode(received):
    R = received
    H = np.array([[1,1,1,0,1,0,0],
        [1,0,1,1,0,1,0],
        [1,1,0,1,0,0,1]])

    Ht = np.transpose(H)
    
    ## Syndromes Calculated with Venn Diagram Equations
    S1 = R[0] + R[1] + R[2] + R[4]
    S2 = R[0] + R[2] + R[3] + R[5]
    S3 = R[0] + R[1] + R[3] + R[6]
    S1 = S1 % 2
    S2 = S2 % 2
    S3 = S3 % 2
    S = [[S1, S2, S3]]

    ## Syndrome calculated with rHt
    Sv = np.dot(R, Ht) % 2
    elocation = -1
    ## Find matching column index in parity matrix
    for i in range(0,7):
        if np.all(Ht[i][:]==Sv): # rHt syndrome
            print('Error detected in position {}'.format(i))
            elocation = i
        else:
            continue
    # for i in range(0,6):
    #     if np.all(Ht[i][:]==S[0]): # Equations syndrome
    #         print(Ht[i], i)
    #     else:
    #         continue

    ## correcting error
    if elocation == -1:
        print('ERROR NOT FOUND')
        R[elocation] = (R[elocation]) % 2
    else:
        R[elocation] = (R[elocation] + 1) % 2
    print('Corrected Codeword: {}'.format(R))

    decoded = R[:4] # message is first four bits

    return decoded

def translate(decodemsgs):
    binstr = ''.join(str(x) for x in decodemsgs[0])
    binstr = binstr + ''.join(str(x) for x in decodemsgs[1])
    translatedcode = chr(int(binstr,2))

    return translatedcode

def processMessage(message):
    print('Encoding and Decoding "{}"'.format(message))
    decodemessage = ''
    for letter in message:
        A = getCodewords(letter)
        code1 = noise(A[0])
        code2 = noise(A[1])
        result = translate([decode(code1), decode(code2)])
        decodemessage += result
    print('\nYour message was {0}'.format(decodemessage))
    return decodemessage

processMessage('Hello')
