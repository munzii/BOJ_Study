import sys

C = int(sys.stdin.readline())

for _ in range(C):
    A = list(map(int, sys.stdin.readline().split()))
    avg = sum(A[1:]) / A[0]
    cnt = 0
    for score in A[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / A[0] * 100
    print("%.3f" %rate + "%")