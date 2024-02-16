import sys

sys.stdin = open("input.txt", "r")

T = int(input())
count = [0] * 31
count[1] = 1
count[2] = 3

def dp(N):
    if count[N] != 0:
        return count[N]
    else:
        count[N] = dp(N - 1) + 2 * dp(N - 2)
        return count[N]


for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case} {dp(n // 10)}')
