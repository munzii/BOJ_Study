import sys

N = int(sys.stdin.readline())
cnt = N

for i in range(N):
    X = sys.stdin.readline()
    for j in range(len(X) - 1):
        if X[j] == X[j + 1]:
            pass
        elif X[j] in X[j + 1:]:
            cnt -= 1
            break
        
print(cnt)