# 1 задача
# В отсортированном массиве с дубликатами найти индекс первого вхождения target. Если нет — -1
# lst = [1,1,1,2,3,3,3,4,5,6,6,6,6,7,8,9,9]
# find_first_index(lst, 3) -> 4




def find_first_index(lst, target):
    left, right = 0, len(lst) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            result = mid
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result

if __name__ == '__main__':
    lst = [1, 1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 7, 8, 9, 9]

    assert find_first_index(lst, 3) == 4
    print("OK")