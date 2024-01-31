import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    k, n, m = map(int, input().split())
    charger = list(map(int, input().split()))

    current_position = 0
    charge_count = 0

    while current_position < n:

        current_position += k

        pre_charger = current_position - k
        forward_range = current_position

        while pre_charger+1 < current_position <= forward_range:
            if current_position in charger:
                charge_count += 1
                break
            current_position -= 1

        if current_position not in charger:
            charge_count = 0
            break

    print(f'#{test_case} {charge_count}')