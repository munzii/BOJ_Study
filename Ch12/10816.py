from collections import Counter
import sys

N = sys.stdin.readline().rstrip()
card = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline().rstrip()
num = list(map(int, sys.stdin.readline().split()))

cnt = Counter(card)

for i in range(len(num)):
    if num[i] in cnt:
        print(cnt[num[i]], end = ' ')
    else:
        print(0, end = ' ')