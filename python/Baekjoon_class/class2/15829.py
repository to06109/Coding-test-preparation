# BOJ 15829 hashing
# 72ms
# 30840KB
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}
L = int(input())
string = input()
result = 0
for i in range(L):
    result += dict[string[i]] * (31 ** i) 

print(result% 1234567891)

# for문에서 매번 1234567891로 나눈 나머지값을 계산하면 50점