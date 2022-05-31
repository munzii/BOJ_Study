from itertools import count

S = input().upper()
S_list = list(set(S))
word = []

for i in S_list:
    cnt = S.count(i)
    word.append(cnt)
    
if word.count(max(word)) > 1:
    print("?")
else:
    print(S_list[word.index(max(word))])