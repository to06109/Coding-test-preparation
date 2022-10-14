from collections import Counter
def solution(nums):
    num = len(nums) // 2
    pocketmons = Counter(nums)
    if len(list(pocketmons)) > num:
        return num
    else:
        return len(list(pocketmons))