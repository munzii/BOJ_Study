import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
S_list = []
for i in range(M, N + 1):
    S = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                S += 1
                break
        if S == 0:
            S_list.append(i)
            
if len(S_list) > 0:
    print(sum(S_list))
    print(min(S_list))
else:
    print(-1)