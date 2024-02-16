import sys
sys.stdin = open("input.txt", "r")

def bfs(s, e):
    stack = [s]

    while stack:
        now = stack.pop()

        if now == e:
            return 1

        if visited[now] == 0:
            visited[now] = 1
            for next in arr[now]:
                # 넓이 탐색에서는 무작정 다 넣어 놓으니까 다른 방향의 노드들이 stack 안에 남아있따!
                if visited[next] == 0:
                    stack.append(next)
    return 0

# bfs처럼 pop을 계속하면 이거는 깊이 탐색이라 해당 깊이의 시작점?만 들어가 있으니까 그 깊이의 시작점이 남아있어야하는데 pop만 되어서 큰일남;;
def dfs(s, e):
    stack = [s]

    while stack:
        # top을 지정하면 굳이 값을 확인한다고 pop하지는 않겠지만 귀찮으니까
        # now = stack.pop()
        now = stack[-1]

        if now == e:
            return 1

        # 해당 인덱스 안에 요소를 다 순회해야 visted 완료한 것으로 보고 1로 바꿈
        if visited[now] == 0:
            # 일단 visted 안 했으면 stack 안에 있어야 새로운 점에 원하는 게 없으면 다시 돌아갈 수 있음
            # stack.append(now)
            for next in arr[now]:
                if visited[next] == 0:
                    stack.append(next)
                    break
            # arr[now]가 비여도 break로 끝난 게 아니니까 else 잘 수행 됨
            # 인접 접점을 다 갔다 와야 visited 한 걸로 봐
            else:
                visited[now] = 1
                stack.pop()

    return 0

def recur_dfs(s, e):
    global cnt
    if s == e:
        cnt = 1
        return cnt
    else:
        if visited[s] == 0:
            for next in arr[s]:
                if visited[next] == 0:
                    recur_dfs(next, e)
            visited[s] = 1
    return cnt

# bfs는 재귀로 못 함.. 선입선출 안 되니까 !!!!

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    cnt = 0

    for i in range(e):
        start, end = map(int, input().split())
        arr[start].append(end)

    target_start, target_end = map(int, input().split())

    print(f'#{test_case} {dfs(target_start, target_end)}')