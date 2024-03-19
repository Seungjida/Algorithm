import sys

sys.stdin = open("sample_input.txt", "r")


def find (stop):
    global cnt
    if stop == n-1:
        return

    if stop + m[stop] >= n-1:
        return

    max_stop = 0
    for i in range(stop+1, stop+m[stop]+1):
        if i < n-1 and m[i] >= m[max_stop]:
            max_stop = i

    cnt += 1
    find(max_stop)
    return

T = int(input())

for tc in range(1, T + 1):
    n, *m = map(int, input().split())

    cnt = 0
    find(0)
    print(f'#{tc} {cnt}')