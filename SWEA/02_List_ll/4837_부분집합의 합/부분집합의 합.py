# import sys
# sys.stdin = open("sample_input.txt", "r")

# 1 << x : 1을 왼쪽으로 x번 shift
# 0(10) -> 1(10), 0001(2) -> 2(10), 0010(2) ...

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for test_case in range(1, T + 1):
    # 몇 개의 원소를 가질지, 원소의 합이 몇 일지 입력 받음
    n, k = map(int, input().split())
    # n,k를 만족하는 부분집합의 개수를 count 변수로 둔다.
    count = 0
    
    # 집합 A의 부분집합의 개수를 비트 연산자로 구하고 이를 범위로 순회하는 for문
    for i in range(1 << len(A)):
        # 어떠한 한 부분집합의 원소를 담을 리스트 변수
        sub = []
        # j가 집합 A의 원소 개수를 범위로 순회하며
        for j in range(len(A)):
            # i번째 부분집합과 비트 & 연산을 했을 때 A의 몇번째 원소의 자리 비트가 1의 결과가 나오는지 알아본다.
            # i의 j번째(뒤에서부터) 비트가 1인 경우, j번 원소
            if i & (1 << j):
                # 1이 나오는 원소를 sub에 추가한다.
                sub.append(A[j])
        # sub의 길이와 합이 조건을 만족하면 count ++
        if len(sub) == n and sum(sub) == k:
            count += 1

    print(f'#{test_case} {count}')
