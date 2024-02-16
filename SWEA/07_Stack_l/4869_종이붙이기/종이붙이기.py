import sys

sys.stdin = open("input.txt", "r")

T = int(input())


def find(target_number, length):
    case = {length: target_number // length}
    if target_number % length != 0:
        case.update(find(target_number % length, 30 - length))
    return case


for test_case in range(1, T + 1):
    n = int(input())
    cases = []
    for i in [10, 20]:
        # 0 ~ 나머지까지 순회하며 케이스 구하기
        cases.append(find(n, i))
    print(cases)

    count = 0
    for case in cases:
        tmp_count = 1
        if 20 in case.keys():
            tmp_count *= 2
        if len(case) == 2:
            tmp_count *= 2
        count += tmp_count

    print(f'#{test_case} {count}')
    '''
    30 -> find
    30 // 10 -> 10:3
    
    * 2
    30 // 20 -> 20:1 , * 2
        10 // 10 -> 10 : 1
        
    [{10:3}, {20:1, 10:1}]
    '''
