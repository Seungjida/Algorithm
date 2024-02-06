import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    soinsu = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0}

    for num, count in soinsu.items():
        while n % num == 0:
            n //= num
            soinsu[num] += 1

    print(f'#{test_case} {" ".join(map(str, soinsu.values()))}')