# 2 задача
# Ограбление домов. В массиве nums указаны деньги в домах. Нельзя грабить два соседних дома. Найти максимальную сумму.
# h = [23,43,1,25]
# rob(h) -> 68
# h = [23,43,1,25, 100]
# rob(h) -> 143

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0
    prev1 = 0

    for money in nums:
        current = max(prev1, prev2 + money)
        prev2 = prev1
        prev1 = current

    return prev1

if __name__ == '__main__':
    assert rob([23, 43, 1, 25]) == 68
    assert rob([23, 43, 1, 25, 100]) == 143
    print("OK")