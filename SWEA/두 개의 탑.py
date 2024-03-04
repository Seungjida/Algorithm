from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m1, m2 = map(int, input().split())
    weights = deque(sorted(list(map(int, input().split())), reverse=True))

    w1 = [0 for _ in range(m1 + 1)]
    w2 = [0 for _ in range(m2 + 1)]
    total_weight = 0

    while weights:
        w = weights.popleft()
        for i in range(1, max(m1, m2) + 1):
            if i <= m1 and w1[i] == 0:
                w1[i] = w
                total_weight += (w1[i] * i)
                break
            elif i <= m2 and w2[i] == 0:
                w2[i] = w
                total_weight += (w2[i] * i)
                break

    print(f'#{tc} {total_weight}')