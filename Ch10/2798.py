import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
x = len(num)
ans = 0

for i in range(0, x - 2):
    for j in range(i + 1, x - 1):
        for k in range(j + 1, x):
            if(num[i] + num[j] + num[k] > M):
                continue
            else:
                ans = max(ans, num[i] + num[j] + num[k])
                
print(ans)