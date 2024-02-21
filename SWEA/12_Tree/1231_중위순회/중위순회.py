# import sys
#
# sys.stdin = open("input.txt", "r")


def solution(now):
    print(element[now], end='')


def in_order(now):
    if now:
        in_order(left[now])
        solution(now)
        in_order(right[now])


for test_case in range(1, 11):
    print(f'#{test_case}', end=' ')
    n = int(input())
    element = [0] * (n + 1)
    left = [0] * (n+1)
    right = [0] * (n+1)

    for _ in range(n):
        index, alpha, *descendant = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        element[index] = alpha
        if len(descendant) >= 1:
            left[index] = descendant[0]
            if len(descendant) == 2:
                right[index] = descendant[1]

    in_order(1)
    print()
