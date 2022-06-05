import sys
import math

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True


for _ in range(int(sys.stdin.readline())):
    T = int(sys.stdin.readline())
    for i in range(T // 2, -1, -1):
        if isPrime(i) and isPrime(T - i):
            print(i, T - i)
            break