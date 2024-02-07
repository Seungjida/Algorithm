# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    stack = []
    input_string = input()

    for element in input_string:
        # 스택이 비어있거나 끝 문자가 element랑 같지 않으면 반복문자가 아니므로 스택에 append
        if len(stack) == 0 or stack[-1] != element:
            stack.append(element)
        else:
            # 이외의 상황은 반복문자이기 때문에 pop()
            stack.pop()
    print(f'#{test_case} {len(stack)}')