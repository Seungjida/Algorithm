# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    a = map(int, list(input()))

    number_card = {}
    for number in a:
        if number in number_card.keys():
            number_card[number] += 1
        else:
            number_card[number] = 1

    max_count = 0
    max_number = 0
    for num, count in number_card.items():
        if count > max_count:
            max_count = count
            max_number = num
        elif count == max_count:
            max_number = max(max_number, num)
            max_count = number_card[max_number]

    print(f'#{test_case} {max_number} {max_count}')