import sys

N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
M.sort()

def binary_search(num):
    x = 0
    y = N - 1
    while x <= y:
        mid = (x + y) // 2
        if M[mid] == num:
            return 1
        elif M[mid] > num:
            y = mid - 1
        else:
            x = mid + 1
    return 0

sys.stdin.readline()

for num in list(map(int, sys.stdin.readline().split())):
    print(binary_search(num), end = ' ')