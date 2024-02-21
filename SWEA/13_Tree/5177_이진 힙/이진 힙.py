import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def insert(new):
    global last
    # 현재 트리에 들어가 있는 마지막 노드의 번호가 last
    # 추가할 거니까 +1
    last += 1
    t[last] = new

    # 현재 노드로부터 조상의 조상을 거슬러 올라가며 최소힙을 만족하는지 검사해야하니까
    # 현재와 현재의 조상 값이 계속 바뀔 것임, 변수로 따로 선언
    now = last
    parent = now // 2

    # 루트 노드가 1부터고 최소힙을 만족하는동안~
    while parent > 0 and t[now] < t[parent]:
        # 값 교환
        t[now], t[parent] = t[parent], t[now]
        # 방금 판단을 마친 부분의 조상을 또 거슬러 올라가야 함
        # now와 parent의 값을 잘 변경했으니까 이제는 parent를 now로 보고 그의 조상을 봄
        now = parent
        parent = now // 2

for test_case in range(1, T + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    last = 0
    t = [0] * (n+1)

    for num in numbers:
        insert(num)

    # 마지막 노드 번호에서 그의 조상으로 거슬러 올라가며 루트까지의 값을 다 더한다아아ㅏ아엉
    sum_ancestor = 0
    now = n//2
    while now != 0:
        sum_ancestor += t[now]
        now //= 2

    print(f'#{test_case} {sum_ancestor}')