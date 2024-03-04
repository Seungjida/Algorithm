# import sys
# sys.stdin = open("sample_input.txt", "r")

def dfs(row, N, total):
    global min_sum

    if total > min_sum:
        return
    if row == N:
        if total < min_sum:
            min_sum = total
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(row+1, N, total+arr[row][i])
                visited[i] = 0

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    min_sum = n * 10
    dfs(0, n, 0)
    print(f'#{test_case} {min_sum}')
