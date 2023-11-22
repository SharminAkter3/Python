def sum_of_odd_numbers(x, y):
    if x > y:
        x, y = y, x

    total_sum = 0

    for num in range(x + 1, y, 1):
        if num % 2 == 1:
            total_sum += num

    return total_sum


t = int(input())

for i in range(0, t, 1):
    x, y = map(int, input().split())
    result = sum_of_odd_numbers(x, y)
    print(result)
