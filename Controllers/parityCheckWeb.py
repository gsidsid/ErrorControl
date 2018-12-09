import numpy as np
from scipy.linalg import solve
import random
import binascii
import time 

def decision(probability):
    return random.random() < probability

def jam(codewords, noise):
    jammed = []
    for letter in codewords:
        if decision(noise):
            controlledMessage = letter
            to_switch = random.randint(0,len(controlledMessage)-1)
            if (controlledMessage[to_switch] == '1'):
                new = list(controlledMessage)
                new[to_switch] = '0'
                jammed.append(''.join(new))
            elif (controlledMessage[to_switch] == '0'):
                new = list(controlledMessage)
                new[to_switch] = '1'
                jammed.append(''.join(new))
        else:
            jammed.append(letter)
    return jammed

def parityCheck(message, noise=0.05):
    binarizedMessage = ' '.join(format(ord(x), 'b') for x in message)
    binarizedLetters = [format(ord(x), 'b') for x in message]
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
    binarizedLettersWithParityBits = []
    for j in range(len(binarizedLetters)):
        binarizedLettersWithParityBits.append(binarizedLetters[j] + str(parities[j]))
    jammed = jam(binarizedLettersWithParityBits, noise)
    decoded = []
    new_parities = []
    for letter in jammed:
        new_parities.append(int(letter[-1]))
        decoded.append(letter[0:-1])
    final = []
    ret = ""
    for message in decoded:
        let = (chr(int(message, 2)))
        final.append(let)
        ret = ''.join(final)
    errs = []
    j = 0
    for message in decoded:
        i = 0
        for bit in message:
            val = int(bit)
            if val == 1:
                i+=1
        if i%2 == 0 and new_parities[j] == 0:
            errs.append(False)
        elif i%2 == 1 and new_parities[j] == 1:
            errs.append(False)
        else:
            errs.append(True)
        j+=1
    errors_detected_idx = [i for i, x in enumerate(errs) if x]
    return [ret, errors_detected_idx]

print(parityCheck("TEST THIS", 0.04))