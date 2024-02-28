from itertools import combinations
T = int(input())
ingredients = []
for i in range(T):
    ingredients.append(list(map(int, input().split())))

min_distance = abs(ingredients[0][0] - ingredients[0][1])
for j in range(1, len(ingredients)+1):
    res = combinations(ingredients, j)
    for k in res:
        sour = 1
        bitter = 0
        for n in k:
            sour *= n[0]
            bitter += n[1]
        min_distance = min(abs(sour-bitter), min_distance)
print(min_distance)