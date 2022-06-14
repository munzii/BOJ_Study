import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M.append((a, b))

M.sort()

for i in range(N):
    print(M[i][0], M[i][1])