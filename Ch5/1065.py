import sys

def hansu(N):
    cnt = 0
    for i in range(1, N + 1):
        N_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif N_list[0] - N_list[1] == N_list[1] - N_list[2]:
            cnt += 1
    return cnt

N = int(sys.stdin.readline())
print(hansu(N))