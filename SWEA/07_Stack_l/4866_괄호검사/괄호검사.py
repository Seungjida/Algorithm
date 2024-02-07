# import sys
#
# sys.stdin = open("input.txt", "r")

class Stack:
    def __init__(self, length):
        self.data = [0] * length
        self.top = -1
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

brackets = {'}': '{', ')': '('}

T = int(input())

for test_case in range(1, T + 1):
    input_code = input()
    stack = Stack(len(input_code))

    is_jjak = True
    for element in input_code:
        if element in brackets.values():
            stack.push(element)
        elif element in brackets.keys():
            if stack.empty():
                is_jjak = False
                break
            else:
                if stack.pop() != brackets[element]:
                    is_jjak = False
                    break
    if not stack.empty():
        is_jjak = False

    print(f'#{test_case} {int(is_jjak)}')
