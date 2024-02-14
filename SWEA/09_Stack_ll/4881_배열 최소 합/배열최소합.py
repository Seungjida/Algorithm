import sys
from itertools import permutations

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    col_list = []
    min_sum = 100

    for i in permutations(range(n), n):
        col_list.append(i)

    for i in col_list:
        temp_sum = 0
        for j in range(n):
            temp_sum += matrix[j][i[j]]
        if temp_sum < min_sum:
            min_sum = temp_sum
    print(f'#{test_case} {min_sum}')