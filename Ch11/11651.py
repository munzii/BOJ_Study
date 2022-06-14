import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M.append((b, a))

M.sort()

for i in range(N):
    print(M[i][1], M[i][0])