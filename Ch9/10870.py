import sys

def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N - 1) + fibonacci(N - 2)

N = int(sys.stdin.readline())
print(fibonacci(N))