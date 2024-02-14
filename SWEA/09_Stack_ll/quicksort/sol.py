def quick_sort(start, end):
    # 언제까지 조사 할거냐
    # stack에 값이 있는 동안
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        if start < end: # 조사 범위가 꼬이지 않았다면
            pivot_index = partition(start, end)
            stack.append((start, pivot_index - 1))    # pivot 왼쪽 조사 대상
            stack.append((pivot_index + 1, end))

def partition(start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1      # 마지막에 pivot위치의 값이 들어가야 할 위치
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

arr = [3, 6, 8, 10, 1, 2, 1]
N = len(arr)
quick_sort(0, N-1)

print(arr)