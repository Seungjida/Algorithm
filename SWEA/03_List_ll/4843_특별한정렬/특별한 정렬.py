import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))


    # 새로운 리스트 생성, 크기만 똑같이
    sorted_a = [0 for _ in range(len(a))]
    # 큰거부터 내림차순으로 짝수번째 인덱스에 넣음
    for des in range(0,len(sorted_a),2):
        # max 씀 당시에 가장 큰 거 넣음
        sorted_a[des] = max(a)
        # 정렬리스트에 넣은 건 뺌
        a.pop(a.index(max(a)))
    # 작은 거부터 오름차순으로 홀수번째 인덱스에 넣음
    for asc in range(1, len(sorted_a), 2):
        # min 씀 당시에 가장 작은 값 넣음
        sorted_a[asc] = min(a)
        # 정렬리스트에 추가한 건 뺌
        a.pop(a.index(min(a)))
    
    # 10개만 출력하고 int list는 join이 안 되니까 str list로 바꾸고 ㅇㅖ쁘게 출력
    print(f'#{test_case} {" ".join(map(str, sorted_a[0:10]))}')