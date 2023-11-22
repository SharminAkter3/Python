def remove_sequence(n, lst):
    numbers = {}
    for num in lst:
        numbers[num] = numbers.get(num, 0) + 1

    removed = 0
    for num, cnt in numbers.items():
        if cnt > num:
            removed += cnt - num
        elif cnt < num:
            removed += cnt

    return removed


n = int(input())
lst = list(map(int, input().split()))

result = remove_sequence(n, lst)
print(result)
