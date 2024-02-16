from collections import deque
# import sys
#
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    pizza_dq = deque(list(enumerate(map(int, input().split()))))
    hwaduk_dq = deque()

    while len(hwaduk_dq) != 1:
        # 화덕에 n만큼 채워져있지 않으면 최대한 채운다.
        if len(hwaduk_dq) <= n:
            while pizza_dq and len(hwaduk_dq) != n:
                target = pizza_dq.popleft()
                hwaduk_dq.append((target[0], target[1]//2))
        # 화덕을 돌린당
        while True:
            target = hwaduk_dq.popleft()
            if target[1] != 0:
                hwaduk_dq.append((target[0], target[1]//2))
            else:
                break
    print(f'#{test_case} {hwaduk_dq.pop()[0]+1}')