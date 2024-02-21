import sys
from collections import deque
sys.stdin = open("input.txt", "r")


def solution(key):
    cal_dict = {'*': lambda x, y: x * y, '/': lambda x, y: x / y,
                '+': lambda x, y: x + y, '-': lambda x, y: x - y}
    
    # 피연산자에 해당하는 값을 배열에 넣을 때 int형으로 넣었으니까
    if type(key) is int:
        cal.append(key)
    # 연산자는 str로 저장되었을고임
    else:
        # 순서가 중요햐용
        num2, num1 = cal.pop(), cal.pop()
        # 문자를 dictionary 키로 넣고 람다 함수로 계산함
        result = cal_dict[key](num1, num2)
        # 계산한 값을 덱에 추가한당
        cal.append(result)


def post_order(now):
    # now가 현재 노드 번호 임당
    if now:
        post_order(left[now])
        post_order(right[now])
        solution(arr[now])


for test_case in range(1, 11):
    n = int(input())
    # 노드에 저장된 값을 나타내는 배열
    arr = [0] * (n + 1)
    # 트리 구성, 부모자식관계 나타내는 배열
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    # 트리를 순회하며 값을 꺼내고 저장할 덱
    cal = deque()

    for _ in range(n):
        node_info = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
        arr[node_info[0]] = node_info[1]
        # 포화 이진이나 완전 이진이가 아니니까 부모,자식 노드 관계를 잘 파악해 놔야함
        if len(node_info) > 2:
            left[node_info[0]] = node_info[2]
            right[node_info[0]] = node_info[3]
    
    # 루트부터 후위순회
    post_order(1)
    # 계산을 마친 값을 integer형으로 바꾼 값 출력
    print(f'#{test_case} {int(cal.pop())}')
