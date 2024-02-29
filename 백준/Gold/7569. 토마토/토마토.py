import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def grow(a):
    global cnt
    for i in range(6):
        if 0<=a[0]+dx[i]<H and 0<=a[1]+dy[i]<N and 0<=a[2]+dz[i]<M:
            new_x, new_y, new_z = a[0]+dx[i], a[1]+dy[i], a[2]+dz[i]
            if tomato[new_x][new_y][new_z] == 0:
                tomato[new_x][new_y][new_z] = a[3]+1
                queue.append((new_x, new_y, new_z, a[3]+1))
    
def find(a):
    max_grow = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if a[i][j][k] > 0:
                    max_grow = max(max_grow, a[i][j][k])
                elif a[i][j][k] == 0:
                    return -1
    return max_grow

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for i in range(N)] for j in range(H)]
queue = deque()
result = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k, 0))
            elif tomato[i][j][k] == 0:
                result = True
while queue:
    now = queue.popleft()
    grow(now)
if result:
    print(find(tomato))
else:
    print(0)