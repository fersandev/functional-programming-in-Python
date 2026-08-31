from itertools import pairwise

def is_sorted(numbers):
    return all(a <= b for a, b in pairwise(numbers))

print(is_sorted([1, 3, 5, 8]))   # True
print(is_sorted([1, 5, 3]))      # False
print(is_sorted([1]))            # True
print(is_sorted([]))             # True
