import sys

N = int(sys.stdin.readline())
M = []

for i in range(N):
    M.append(int(sys.stdin.readline()))
    
for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]
            
for n in M:
    print(n)