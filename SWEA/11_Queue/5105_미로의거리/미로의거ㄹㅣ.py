from collections import deque
import sys

sys.stdin = open("input.txt", "r")

T = int(input())

# 대각선은 안 봐도 되겠지
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]


def bfs(start):
    dq = deque([start])
    count_list = []

    # 몇 번째로 방문하는지 어떻게 계산해야할지 몰라서 헤맴
    # dfs로도 도전했었는데 다른 데를 다 방문하지 않았는데 visited를 1로 할 수도 없고...
    # 또 visited를 0으로 하면 델타 탐색으로 다시 돌아가겠지요..
    while dq:
        now = dq.popleft()
        visited[now[0]][now[1]] += 1

        for movement in range(4):
            ni = now[0] + di[movement]
            nj = now[1] + dj[movement]
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 3:
                    count_list.append(visited[now[0]][now[1]]-1)
                if visited[ni][nj] == 0 and arr[ni][nj] == 0:
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

    # 출발점에서 도착점까지 델타 탐색 + bfs
    print(f'#{test_case} {bfs(start)}')