# import sys
# sys.stdin = open("input.txt", "r")

class Stack:
    def __init__(self, length):
        self.data = [0] * length
        self.top = -1

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def get(self):
        if not self.empty():
            return self.data[self.top]

    def push(self, item):
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if not self.empty():
            self.top -= 1
            return self.data[self.top + 1]

    def __str__(self):
        return f'{"".join(self.data[:self.top + 1])}'


for test_case in range(1, 11):
    n, input_string = input().split()
    # 문자열로 들어가 있으니까 int()를 이용해 n을 int형으로 변환
    st = Stack(int(n))
    
    # 입력 받은 문자열을 순회하며 문자를 얻고 그것을 stack안의 마지막 element와 비교한다.
    for number in input_string:
        if st.empty():
            st.push(number)
        else:
            if st.get() != number:
                st.push(number)
            else:
                # 마지막 element와 같지 않거나 empty가 될 때까지 마지막 element를 pop한다
                # 현재 number은 push하면 안 됨
                while st.get() == number and not st.empty():
                    st.pop()

    print(f'#{test_case} {st}')
