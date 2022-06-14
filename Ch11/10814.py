import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    M.append((a, b))
    
M.sort(key = lambda x : x[0])

for i in M:
    print(i[0], i[1])