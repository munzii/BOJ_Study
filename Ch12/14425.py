import sys

N, M = map(int, sys.stdin.readline().split())
arr = dict()
cnt = 0

for _ in range(N):
    x = sys.stdin.readline()
    arr[x] = True

for _ in range(M):
    y = sys.stdin.readline()
    if y in arr.keys():
        cnt += 1
        
print(cnt)