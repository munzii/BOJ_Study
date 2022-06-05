import sys

N = int(sys.stdin.readline())
X = map(int, sys.stdin.readline().split())
cnt = 0

for i in X:
    S = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                S += 1
        if S == 0:
            cnt += 1

print(cnt)