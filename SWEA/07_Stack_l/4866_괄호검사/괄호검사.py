# import sys
# sys.stdin = open("input.txt", "r")

class Stack:
    def __init__(self, length):
        self.data = [0] * length
        self.top = -1
        # length를 벗어난 push 요청이 들어올 수도 있으니까 일단 length 인스턴스 변수도 생성함
        self.length = length

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def get(self):
        if not self.empty():
            return self.data[self.top]

    def push(self, item):
        if self.top < self.length:
            self.top += 1
            self.data[self.top] = item

    def pop(self):
        if not self.empty():
            self.top -= 1
            return self.data[self.top + 1]

    def __str__(self):
        return f'{self.data}'

# 괄호들을 서로 짝이 맞게 dictionary에 저장
brackets = {'}': '{', ')': '('}

T = int(input())

for test_case in range(1, T + 1):
    input_code = input()
    stack = Stack(len(input_code))

    is_jjak = True
    for element in input_code:
        # 만약 열린 괄호면
        if element in brackets.values():
            # 스택에 추가
            stack.push(element)
        # 만약 닫힌 괄호면
        elif element in brackets.keys():
            # 빈 stack은 pop할 수 없으니까 오류
            if stack.empty():
                is_jjak = False
                break
            else:
                # pop한 것이 해당 괄호의 짝이 아니라면 오류
                if stack.pop() != brackets[element]:
                    is_jjak = False
                    break
    # 입력받은 문자열을 다 돌았는데 stack이 비지 않으면 짝이 안 맞은 거니까 오류
    if not stack.empty():
        is_jjak = False

    print(f'#{test_case} {int(is_jjak)}')
