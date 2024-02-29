def backtracking(row):
    # global count
    # if row == n:
    #     count += 1
    # else:
    #     for j in range(n):
    #         if visited[row][j] == 0:
    #             visited[row][j] = 1
    #             for v in range(8 * n):
    #                 ni = row + (di[v % 8] * (v // 8 + 1))
    #                 nj = j + (dj[v % 8] * (v // 8 + 1))
    #                 if 0 <= ni < n and 0 <= nj < n:
    #                     visited[ni][nj] = 1
    #             backtracking(row + 1)
    #             visited[row][j] = 0
    #             for v in range(8 * n):
    #                 ni = row + (di[v % 8] * (v // 8 + 1))
    #                 nj = j + (dj[v % 8] * (v // 8 + 1))
    #                 if 0 <= ni < n and 0 <= nj < n:
    #                     visited[ni][nj] = 0

n = int(input())
visited = [[0] * n for _ in range(n)]
count = 0
di = [0,0,1,-1,1,1,-1,-1]
dj = [1,-1,0,0,1,-1,1,-1]
backtracking(0)
print(count)