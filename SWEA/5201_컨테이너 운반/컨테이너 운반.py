# import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # 컨테이너 수, 트럭 수
    n, m = map(int, input().split())
    # 각 컨테이너에 실린 화물의 무게
    weights = deque(sorted(map(int, input().split()), reverse=True))
    # 트럭의 적재용량
    trucks = deque(sorted(map(int, input().split()), reverse=True))

    moved = 0
    while trucks and weights:
        w = weights[0]
        t = trucks[0]
        if t >= w:
            moved += weights.popleft()
            trucks.popleft()
        else:
            weights.popleft()

    print(f'#{tc} {moved}')
