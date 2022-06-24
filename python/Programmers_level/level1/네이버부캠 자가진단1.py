from collections import Counter
arr = [3, 5, 7, 9, 1]
result = []
dict = Counter(arr)
key = dict.keys()
for i in key:
    if dict[i] != 1:
        result.append(dict[i])

if len(result) == 0:
    result.append(-1)
print(result)
