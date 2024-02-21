import sys

sys.stdin = open("input.txt", "r")

T = int(input())

# 서브트리의 노드 개수 count
def find(now):
    global cnt
    # 현재의 값이 존재하는 노드라면
    if now:
        # 노드++
        cnt += 1
        # 왼쪽 자식 노드부터 탐색
        find(des[now][0])
        # 오른쪽 자식 노드 탐색
        find(des[now][1])


for test_case in range(1, T + 1):
    # 간선의 개수와 서브 트리의 노드 개수를 찾고 싶은 노드 n을 입력받음
    e, n = map(int, input().split())
    # 부모 자식 번호 쌍을 담은 리스트
    ssang = list(map(int, input().split()))

    # 1~노드개수의 값을 담은 t
    t = [i for i in range(e + 2)]
    # 해당 인덱스 노드의 자식 노드들을 담을 des
    des = [[0, 0] for _ in range(e + 2)]

    # des에 알맞은 값을 할당한다
    # 안 들어가면 자식 노드가 없는 거고.. 0이 들어가 있겠지?
    for i in range(e):
        if not des[ssang[i * 2]][0]:
            des[ssang[i * 2]][0] = ssang[i * 2 + 1]
        else:
            des[ssang[i * 2]][1] = ssang[i * 2 + 1]

    # 서브 트리 안 노드의 개수를 셀 변수 cnt
    cnt = 0
    # 노드 n의 서브트리를 순회하며 노드의 개수를 세어보자!
    find(n)
    print(f'#{test_case} {cnt}')
