# import sys
# sys.stdin = open("algo1_sample_in.txt", "r")

def change_to_hex(cnt, num):
    # 이진수와 16진수를 짝지은 딕셔너리
    bin_to_hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                  '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                  '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                  '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    result = ""
    # 이진수를 4개씩보며 딕셔너리에 있는 값과 짝지어 16진수로 변환한다.
    for index in range(0,cnt,4):
        result += bin_to_hex[num[index:index+4]]
    return result

def change_to_bin(num):
    # 16진수와 이진수를 짝지은 딕셔너리
    hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                  '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                  '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                  'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    result = ""
    # 숫자를 하나하나보며 딕셔너리에 있는 값과 짝지어 이진수로 변환한다.
    for number in num:
        result += hex_to_bin[number]
    return result

T = int(input())
for tc in range(1, T+1):
    n, num = input().split()
    cnt = int(n)

    # 만약 이진수면 24자리일 것이고,
    if cnt == 24:
        print(f'#{tc} {change_to_hex(cnt, num)}')
    # 만약 16진수이면 6자리 일 것이다.
    elif cnt == 6:
        print(f'#{tc} {change_to_bin(num)}')