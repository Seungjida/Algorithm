import sys
sys.stdin = open("sample_input.txt", "r")

# 시간 초과가 나욤, 7개 맞았따능..
def back_tracking(stop, cnt):
    global min_cnt
    if stop == n-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    # 가지치기 해줘야 시간 초과가 안 나욤
    # 더 큰 건 볼 필요 없잖아
    if cnt >= min_cnt:
        return

    # 현재 stop으로부터 갈 수 있는 stop(index)까지만 계산
    for i in range(stop, stop + m[stop]+1):
        if i >= n:
            return

        if visited[i] == 0:
            visited[i] = 1
            back_tracking(i, cnt + 1)
            visited[i] = 0
    return

T = int(input())

for tc in range(1, T+1):
    n, *m = map(int, input().split())
    visited = [0] * n

    # 다 방문한다치면
    min_cnt = n-1
    back_tracking(0, 0)
    # 시작 stop도 cnt 되어서 1은 빼줌
    print(f'#{tc} {min_cnt-1}')