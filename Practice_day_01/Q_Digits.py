def right_to_left(N):
    digits = []
    while N > 0:
        digits.append(N % 10)
        N //= 10
    print(*digits[::])


T = int(input())

for i in range(0, T, 1):
    N = int(input())
    right_to_left(N)
