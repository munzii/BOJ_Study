import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    M.append(int(sys.stdin.readline()))
    
for i in range(1, len(M)):
    while (i > 0) & (M[i] < M[i - 1]):
        M[i], M[i - 1] = M[i - 1], M[i]
        i -= 1
        
for n in M:
    print(n)