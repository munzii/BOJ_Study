import sys

N = int(sys.stdin.readline())
M = []

for i in str(N):
    M.append(i)
    
M.sort(reverse = True)

print("".join(M))