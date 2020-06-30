#!/usr/bin/python3

# Using dictionaries
def find_pairs(numbers, target):
    di = {}
    for i, n in enumerate(numbers):
        complement = target - n
        if complement in di:
            return f'{n} y {complement}'
        di[n] = i
    return 'Pairs of numbers are not found'

# Using sets
# def find_pairs(numbers, target):
#     s = set()
#     for num in numbers:
#         if target - num in s:
#             return(f'{num} y {complement})
#         s.add(num)
#     return 'Pairs of numbers are not found'

print(find_pairs([14, 6, 2, 8, 10, 1, 13], 14))
print(find_pairs([14, 6, 2, 8, 10, 1, 13], 22))
print(find_pairs([14, 6, 2, 8, 10, 1, 13], 4))
print(find_pairs([14, 6, 2, 8, 10, 1, 13], 13))
