import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

# 중위탐색을 하며 방문한 순서대로 dq.popleft()를 하며 노드의 값을 업데이트 함
def solution(now):
    t[now] = dq.popleft()

def in_order(now):
    if now:
        in_order(left[now])
        solution(now)
        in_order(right[now])

for test_case in range(1, T+1):
    n = int(input())

    # 트리에 저장해야하는 값들을 덱에 순서대로 저장
    dq = deque(range(1,n+1))
    # 트리를 만들고 값을 0으로 초기화
    t = [0] * (n+1)

    # 왼/오른쪽 자식노드를 저장할 배열 0으로 초기화
    left = [0] * (n+1)
    right = [0] * (n+1)
    # 어떤 한 노드가 어떤 자식노드를 가지는지 본다
    # 이진 탐색 트리니까 트리의 마지막 인덱스의 부모 인덱스까지가 바로 전 레벨
    # 마지막 인덱스가 들어간 레벨은 리프 노드임
    for i in range(1, n//2+1):
        if i*2 <= n:
            left[i] = i*2
        if i * 2 +1 <= n:
            right[i] = i * 2 +1

    # 중위탐색 진행하며 노드의 값을 채움
    in_order(1)
    print(f'#{test_case} {t[1]} {t[n//2]}')