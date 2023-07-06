from collections import Counter
d = dict(Counter(input().upper().strip()))
result = []
for i in d.keys():
    if d[i] == max(d.values()):
        result.append(i)
if len(result) > 1:
    print("?")
else:
    print(result[0])