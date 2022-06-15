import sys

N, M = map(int, sys.stdin.readline().split())

x = {}
y = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    x[i] = name
    y[name] = i
    
for _ in range(M):
    pkm = sys.stdin.readline().strip()
    if pkm.isdigit() == True:
        print(x[int(pkm) - 1])
    else:
        print(y[pkm] + 1)