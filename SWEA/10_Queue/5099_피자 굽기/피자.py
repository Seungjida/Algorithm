from collections import deque
import sys

sys.stdin = open("sample_input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pz = list(map(int, input().split()))

    pzz = deque([(pz[i], i+1) for i in range(M)])
    que = deque([])
    for _ in range(N):
        que.append(pzz.popleft())

    while len(que) != 1:
        current = que.popleft()
        cz = current[0]
        cz //= 2

        if cz:
            que.append((cz, current[1]))
        if len(que) < N and pzz:
            que.append(pzz.popleft())
    print(f'#{tc} {que.pop()[1]}')