import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def binarysearch(r, find):
    count = 0
    l = 1
    while True:
        # 한 번이라도 중간값을 계산하면 count++
        c = (l + r) // 2
        count += 1

        # 찾고자 하는 값이 중간값보다 크면 중간값 이후에 나오니까 left값을 방금 구한 중간값으로 업뎃
        if find > c:
            l = c
        # 찾고자 하는 값이 중간값보다 작으면 중간값 이전에 나오니까 right값을 방금 구한 중간값으로 업뎃
        elif find < c:
            r = c
        # 찾으면 while문 탈출
        else:
            break
    return count


for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    a_find_cnt = binarysearch(P, A)
    b_find_cnt = binarysearch(P, B)

    print(f'#{test_case}', end=' ')
    # 횟수가 작은 게 빨리 찾은 거니까 ㅎㅎㅎ
    if a_find_cnt < b_find_cnt:
        print('A')
    elif a_find_cnt > b_find_cnt:
        print('B')
    else:
        print(0)
