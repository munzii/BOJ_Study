import sys

N = int(sys.stdin.readline())
M = [0] * 10001

for _ in range(N):
    M[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if M[i] != 0:
        for j in range(M[i]):
            print(i)