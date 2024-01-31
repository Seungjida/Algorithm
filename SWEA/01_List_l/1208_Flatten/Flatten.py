import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    for i in range(dump):
        # 순서 상관없으니까 상자의 순서를 높이의 오름차순으로 정렬한다.
        heights.sort()
        # 만약 모두 같은 높이라면 평탄화가 완료되었으므로 루프를 탈출한다.
        if len(set(heights)) == 1:
            break
        # 덤프한다
        heights[0] += 1
        heights[-1] -= 1

    # 주어진 횟수만큼 덤프를 진행한 후 상자들의 높이를 정렬한다.
    heights.sort()
    # 최고점과 최저점의 차이를 구한다.
    distance = heights[-1] - heights[0]
    # 출력한다.
    print(f'#{test_case} {distance}')
