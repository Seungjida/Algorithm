import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)

    sum_max = 0
    for c in range(k):
        sum_max += scores[c]

    print(f'#{tc} {sum_max}')