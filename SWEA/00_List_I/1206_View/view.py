#import sys
#sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    T = int(input())
    buildings = list(map(int, input().split()))

    count = 0
    for number in range(2, len(buildings) - 2):
        left_max = max(buildings[number - 2], buildings[number - 1])
        right_max = max(buildings[number + 2], buildings[number + 1])

        if (buildings[number] - left_max >= 0) and (buildings[number] - right_max >= 0):
            count += min((buildings[number] - left_max), (buildings[number] - right_max))

    print(f'#{test_case} {count}')


# 5개씩 한번에 봐도 됨