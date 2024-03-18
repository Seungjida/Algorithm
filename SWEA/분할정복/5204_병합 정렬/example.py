# 최소 단위가 될 때까지 균등한 크기로 분할 -> 부분 리스트들을 정렬하면서 병합

unsorted_list = [int(x) for x in input().split()]


def merge_sort(unsorted_list):
    # 크기가 1이하면 바로 반환, 정렬할 필요 없어
    if len(unsorted_list) <= 1:
        return unsorted_list

    # 리스트를 2분할
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    # 2분할한 리스트를 각각 merge sort진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)

    # 정렬한 리스트를 받는 것과 동시에 리턴
    # left_나 right의 길이가 1보다 크면 이 값이 반환되어 들어갈 것임
    # 재귀를 호출한 거니께?
    # 최종적으로 이 함수를 탈출할 때에도 이 부분이 리턴
    return merge(left_, right_)

def merge(left, right):
    i, j = 0, 0
    sorted_list = []

    # left와 right에 서로 비교할 값이 남아 있을 때까지
    # 더 작은 거 골라서 sorted_list에 추가, 인덱스 증가시킴
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    # left는 남았는데 right에 이것과 비교할 값이 없다!(right의 모든 요소가 남은 left 요소보다 작겠지)
    # 그럼 걍 정렬되어있는 left를 끝까지 sorted_list에 이어서 추가
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    # right는 남았는데 left에 이것과 비교할 값이 없다!
    # 그럼 걍 정렬되어있는 right를 끝까지 sorted_list에 이어서 추가
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    # 일단 정렬한 리스트 반환
    return sorted_list

print(merge_sort(unsorted_list))