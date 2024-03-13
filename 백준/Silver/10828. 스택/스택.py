import sys
n = int(input())

stack = []
top = -1

def push(x):
    global top
    stack.append(x)
    top += 1

def f_pop():
    # list.pop()도 리스트에 아이템이 없으면 index error 일으킴 알고 있으라구ㅜ오
    global top
    if stack:
        print(stack.pop())
        top -= 1
    else:
        print(-1)


def size():
    print(len(stack))


def empty():
    if not stack:
        print(1)
    else:
        print(0)


def f_top():
    if stack:
        print(stack[top])
    else:
        print(-1)


for _ in range(n):
    inputs = list(sys.stdin.readline().split())
    command = inputs[0].lower()

    # match - case 안 됨..?

    try:
        if command == 'push':
            push(int(inputs[1]))
        elif command == 'pop':
            f_pop()
        elif command == 'size':
            size()
        elif command == 'empty':
            empty()
        elif command == 'top':
            f_top()
        else:
            raise Exception('잘못된 입력값입니다.')
    except Exception as e:
        print(e)