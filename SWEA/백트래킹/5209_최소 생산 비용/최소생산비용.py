import sys
sys.stdin = open("sample_input.txt", "r")

def backtracking(row, now_cost):
    global min_cost
    if row == n:
        if now_cost < min_cost:
            min_cost = now_cost
        return

    if now_cost > min_cost:
        return
    
    # i는 col 말하는 겨! 중복 안 됩니데이
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(row+1, now_cost + v[row][i])
            visited[i] = 0

    return

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n

    min_cost = 99 * n
    backtracking(0, 0)
    print(f'#{tc} {min_cost}')