import sys
sys.stdin = open("input.txt", "r")

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sum_list = []
    right_diagonal_sum = 0
    left_diagonal_sum = 0

    for i in range(100):
        right_diagonal_sum += arr[i][i]
        left_diagonal_sum += arr[i][99 - i]

        i_row_sum = sum(arr[i])

        i_col_sum = sum([arr[j][i] for j in range(100)])
        sum_list.extend([i_row_sum, i_col_sum])

    sum_list.extend([right_diagonal_sum, left_diagonal_sum])

    print(f'#{test_case} {max(sum_list)}')