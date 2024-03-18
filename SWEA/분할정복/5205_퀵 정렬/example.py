def 재귀_빈배열(arr):
    if len(arr) <= 1:
        return arr
    # 중간 것을 피봇값으로..
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return 재귀_빈배열(lesser_arr) + equal_arr + 재귀_빈배열(greater_arr)


def 파이썬_장점_활용(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환

    return 파이썬_장점_활용(left_side) + [pivot] + 파이썬_장점_활용(right_side)


def 정석(array, start, end):
    if start >= end:
        return
    pivot = start  # 피벗 초기값은 첫번째 요소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

            # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:  # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    정석(array, start, right - 1)
    정석(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
