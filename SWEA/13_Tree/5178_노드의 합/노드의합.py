import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def post_order(now):
    if 0 < now <= n:
        # 후위순회를 돌며 노드의 값을 찾는데,
        # 리프 노드 이외의 노드들만 노드의 값을 찾아준다.
        if t[now] == 0:
            t[now] = post_order(now * 2) + post_order(now * 2 + 1)
        # 값이 뭔가 들어가 있으면 그 값을 리턴~
        return t[now]
    # 노드 개수를 초과하더라도 일단 함수에 들어오긴 하니까 0을 리턴해 오류가 안 나도록 함
    return 0

for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    t = [0] * (n + 1)
    
    # 리프 노드의 값을 받아서 t에 알맞게 넣어줌
    for _ in range(m):
        index, number = map(int, input().split())
        t[index] = number

    post_order(1)
    print(f'#{test_case} {t[l]}')
