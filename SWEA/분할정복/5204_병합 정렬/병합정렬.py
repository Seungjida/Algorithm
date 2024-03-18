import sys
sys.stdin = open("sample_input.txt", "r")


def merge(left, right):
    global cnt
    i = j = 0
    sorted_list = []

    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list

    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left, right)

T = int(input())

for tc in range(1 ,T+1):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    final_list = merge_sort(a)
    print(f'#{tc} {final_list[len(final_list)//2]} {cnt}')