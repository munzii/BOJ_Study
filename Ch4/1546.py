import sys

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
Max_S = max(S)

for i in range(N):
    S[i] = S[i] / Max_S * 100
    
print(sum(S) / N)