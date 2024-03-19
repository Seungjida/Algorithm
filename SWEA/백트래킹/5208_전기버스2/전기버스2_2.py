import sys

sys.stdin = open("sample_input.txt", "r")

def back_tracking(stop, cnt):
    global min_cnt
    if stop == n-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    # 현재 위치부터 갈 수 있는 최대 정류장
    farthest_stop = min(stop + m[stop], n - 1)

    # 목적지와의 거리 비교를 통한 가지치기
    if farthest_stop >= n - 1:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    for i in range(stop + 1, farthest_stop + 1):
        if visited[i] == 0:
            visited[i] = 1
            back_tracking(i, cnt + 1)
            visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    n, *m = map(int, input().split())
    visited = [0] * n

    min_cnt = n-2
    back_tracking(0, 0)
    print(f'#{tc} {min_cnt}')
