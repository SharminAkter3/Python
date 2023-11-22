# n = int(input())
# arr = list(map(int, input().split()))

# count = 0

# while True:
#     flag = True
#     for i in range(0, n):
#         if arr[i] % 2 == 0:
#             result = arr[i] // 2
#             arr[i] = result
#         else:
#             flag = False
#             break
#     if flag == True:
#         count += 1
#     else:
#         break

# print(count)

n = int(input())
arr = list(map(int, input().split()))

count = 0

while True:
    even = True
    for i in range(0, n):
        if arr[i] % 2 == 0:
            result = arr[i] // 2
            arr[i] = result
        else:
            even = False
            break
    if even == True:
        count += 1
    else:
        break

print(count)
