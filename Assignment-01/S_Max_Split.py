# s = input()
# cnt = 0
# match_cnt = 0
# matching_string = ""

# for char in s:
#     if char == "L":
#         cnt += 1
#     else:
#         cnt -= 1
#     if cnt == 0:
#         match_cnt += 1
# print(match_cnt)
# for char in s:
#     if char == "L":
#         cnt += 1
#         matching_string += char
#     else:
#         cnt -= 1
#         matching_string += char
#     if cnt == 0:
#         match_cnt += 1
#         print(matching_string)
#         matching_string = ""

s = input()
count = 0
match = 0
store_match = ""

for char in s:
    if char == "L":
        count += 1
    else:
        count -= 1
    if count == 0:
        match += 1
print(match)
for char in s:
    if char == "L":
        count += 1
        store_match += char
    else:
        count -= 1
        store_match += char
    if count == 0:
        match += 1
        print(store_match)
        store_match = ""
