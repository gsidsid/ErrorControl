import numpy as np 
import random

G = np.array([[1,0,0,0,1,1,1],
    [0,1,0,0,1,0,1],
    [0,0,1,0,1,1,0],
    [0,0,0,1,0,1,1]])

M = np.array([[0,0,1,0]])


print(G)
print(M)
R = np.dot(M,G)
print(R)
error = random.randint(0,6)
print(R[0][error], error)
R[0][error] = (R[0][error] + 1) % 2
print(R[0][error], error)
print(R)
K = [0,1,0,0,1,0,1]

for i in range(0,3):
    if np.all(G[i][:]==K):
        print(G[i], i)
    else:
        continue

P = np.array([[1,1,1,0,1,0,0],
    [1,0,1,1,0,1,0],
    [1,1,0,1,0,0,1]])
    
P = np.transpose(P)

print(P)

S1 = R[0][0] + R[0][1] + R[0][2] + R[0][4]
print(S1)
print((S1 % 2))
S2 = R[0][0] + R[0][2] + R[0][3] + R[0][5]
print(S2)
print((S2 % 2))
S3 = R[0][0] + R[0][1] + R[0][3] + R[0][6]
print(S3)
print((S3 % 2))

S1 = S1 % 2
S2 = S2 % 2
S3 = S3 % 2
S = [[S1, S2, S3]]

for i in range(0,6):
    if np.all(P[i][:]==S[0]):
        print(P[i], i)
    else:
        continue
