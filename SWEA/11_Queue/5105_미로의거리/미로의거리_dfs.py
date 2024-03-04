# 그냥 연습
from collections import deque
# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


def dfs(start):
    dq = deque([start])
    count_list = []
    
    while dq:
        now = dq.pop()
        visited[now[0]][now[1]] += 1

        for i in range(4):
            ni = now[0] + di[i]
            nj = now[1] + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 3:
                    count_list.append(visited[now[0]][now[1]]-1)
                    break
                elif arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    dq.append([ni, nj])
                    visited[ni][nj] = visited[now[0]][now[1]]
    if count_list:
        return min(count_list)
    else:
        return 0
    

for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    # 출발점 좌표 찾아
    start = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start = [i, j]
                break
        if start:
            break

    print(f'#{test_case} {dfs(start)}')
