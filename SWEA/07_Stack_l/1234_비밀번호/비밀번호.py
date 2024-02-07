import sys

sys.stdin = open("input.txt", "r")


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
    st = Stack(int(n))

    for number in input_string:
        if st.empty():
            st.push(number)
        else:
            if st.get() != number:
                st.push(number)
            else:
                while st.get() == number and not st.empty():
                    st.pop()

    print(f'#{test_case} {st}')
