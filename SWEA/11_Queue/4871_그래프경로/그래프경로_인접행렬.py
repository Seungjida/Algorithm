import sys
sys.stdin = open("input.txt", "r")

def bfs(s,e):
    stack = [s]

    while stack:
        now = stack.pop()
        if now == e:
            return 1
        else:
            if visited[now] == 0:
                visited[now] = 1
                # range로 도는 거.. 잘 생각 해 !
                for next in range(1, v+1):
                    if visited[next] == 0 and arr[now][next] == 1:
                        stack.append(next)
    return 0

def dfs(s,e):
    stack = [s]

    while stack:
        now = stack.pop()
        if now == e:
            return 1
        else:
            if visited[now] == 0:
                stack.append(now)
                for next in range(1, v+1):
                    if visited[next] == 0 and arr[now][next] == 1:
                        stack.append(next)
                        break
                else:
                    visited[now] = 1
    return 0

def recur_dfs(s, e):
    global cnt
    if arr[s][e] == 1 or s == e:
        cnt = 1
        return cnt
    else:
        # 어차피 index 순서대로 도니까 11번 라인에 if문 필요 없을 거 같기도 하고...
        if visited[s] == 0:
            for next in range(1, v+1):
                if visited[next] == 0 and arr[s][next] == 1:
                    recur_dfs(next, e)
            visited[s] = 1
    return cnt

def recur_dfs2(s, e):
    global cnt
    visited[s] = 1

    if arr[s][e] == 1 or s == e:
        cnt = 1
        return cnt
    else:
        for next in range(1, v + 1):
            if visited[next] == 0 and arr[s][next] == 1:
                recur_dfs(next, e)
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    # arr의 인덱스는 해당 노드, arr[i]은 i와 인접 가능한 노드들을 담은 배열(v개), arr[i][t]는 i->t이면 1
    arr = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)
    cnt = 0

    for i in range(e):
        start, end = map(int, input().split())
        arr[start][end] = 1

    target_start, target_end = map(int, input().split())

    print(f'#{test_case} {dfs(target_start, target_end)}')