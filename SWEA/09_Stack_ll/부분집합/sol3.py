from itertools import permutations

a = range(1, 11)
b = list(permutations(a, 3))
print(b)