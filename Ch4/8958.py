import sys

T = int(sys.stdin.readline())


for i in range(T):
    A = sys.stdin.readline()
    score = 0
    sumScore = 0
    for j in A:
        if j == "O":
            score += 1
        else:
            score = 0
        sumScore += score
    print(sumScore)