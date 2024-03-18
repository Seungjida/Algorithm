import sys
sys.stdin = open("sample_input.txt", "r")

def merge(left, right):
    global cnt
    i = j = 0
    sorted_list = []

    # 이거 안 됨, 스택에서는 뒤에서만 빼니까 첨에 모든 걸 분할ㅇ해서 넣었다쳐도 맨 병합되는 과정에서 모든 코드를 돌아보지 않음
    # 그러니까 분할이 제대로 안 되어서 이게 안 된다는 뜻
    # if left[-1] > right[-1]:
    #     cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def merge_sort(unsorted_list):
    stack = [[x] for x in unsorted_list]  # 각 원소를 개별 리스트로 스택에 저장

    while len(stack) > 1:
        left = stack.pop()
        right = stack.pop()
        stack.append(merge(left, right))

    return stack[0]

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    cnt = 0
    final_list = merge_sort(list(map(int, input().split())))
    print(f'#{tc} {final_list[n // 2]} {cnt}')
