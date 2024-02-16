from collections import deque
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    dq = deque(map(int, input().split()))

    for i in range(m):
        target = dq.popleft()
        dq.append(target)

    print(f'#{test_case} {dq.popleft()}')