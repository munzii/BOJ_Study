import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    M.append(sys.stdin.readline().strip())

set_M = set(M)
M = list(set_M)
M.sort()
M.sort(key = len)

for i in M:
    print(i)