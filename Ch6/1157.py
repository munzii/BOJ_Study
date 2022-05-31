import sys

S = sys.stdin.readline().upper()
S_list = list(set(S))
word = []

for i in S_list:
    cnt = S.count
    word.append(cnt(i))
    
if word.count(max(word)) > 1:
    print("?")
else:
    print(S_list[(word.index(max(word)))].upper())