import sys
sys.stdin = open("sample_input.txt", "r")

def binary_search(N, target):
    start = 0
    end = n - 1
    side = None
    find = False

    while start <= end and not find:
        middle = (start + end)//2

        if N[middle] < target and side != "right":
            start = middle + 1
            side = "right"
        elif N[middle] > target and side != "left":
            end = middle - 1
            side = "left"
        elif N[middle] == target:
            find = True
        else:
            break
    return find

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    N = list(map(int, input().split()))
    N.sort()
    M = list(map(int, input().split()))
    cnt = 0

    for target in M:
        if binary_search(N, target):
            cnt += 1

    print(f'#{tc} {cnt}')