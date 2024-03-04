import sys
sys.stdin = open("input.txt", "r")

def dp(N):
    if N == 0:
        count[0] = 0
    elif N == 1:
        count[1] = 1
    else:
        count[n] = dp(N-1) + (2 * dp(N-2))

T = int(input())

count = [0] * 31
for test_case in range(1, T+1):
    n = int(input())
    dp(n//10)
print(f'#{test_case} {count[n//10]}')