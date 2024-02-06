import sys

sys.stdin = open("input.txt", "r")


def is_palindrome_in_row(words):
    for row in range(n):
        for i in range(0, n - m + 1):
            original = words[row][i:i + m]
            reverse = original[::-1]

            if original == reverse:
                return original
    return None


def is_palindrome_in_col(words):
    for col in range(n):
        col_str = ''.join([words[i][col] for i in range(n)])
        for j in range(0, n - m + 1):
            original = col_str[j:j + m]
            reverse = original[::-1]

            if original == reverse:
                return original
    return None


T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    word_list = [input() for _ in range(n)]

    print(f'#{test_case}', end=' ')
    if is_palindrome_in_row(word_list) is not None:
        print(is_palindrome_in_row(word_list))
    elif is_palindrome_in_col(word_list) is not None:
        print(is_palindrome_in_col(word_list))
