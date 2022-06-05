import sys
import math

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

n_list = list(range(2, 246912))
p_list = []

for i in n_list:
    if isPrime(i):
        p_list.append(i)
        
n = int(sys.stdin.readline())

while n != 0:
    cnt = 0
    for i in p_list:
        if n < i <= n * 2:
            cnt +=1
    print(cnt)
    n = int(sys.stdin.readline())