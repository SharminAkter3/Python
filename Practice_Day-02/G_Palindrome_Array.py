def is_palindrome(a):
    return a == a[::-1]


n = int(input())
val = list(map(int, input().split()))

if is_palindrome(val):
    print("YES")
else:
    print("NO")
