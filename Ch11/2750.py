import sys

N = int(sys.stdin.readline())
M =[]

for i in range(N):
    M.append(int(sys.stdin.readline()))

M = sorted(M)

for i in range(len(M)):
    print(M[i])