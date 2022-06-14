from collections import Counter
import sys

N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))
    
M.sort()

cnt = Counter(M).most_common(2)

print(round(sum(M) / len(M)))
print(M[len(M) // 2])

if len(M) > 1:
    if cnt[0][1] == cnt [1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
    
print(max(M) - min(M))