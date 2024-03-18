T = int(input())

# 피봇과 값을 비교해 작은 값들을 담은 리스트, 동일한 값을 담은 리스트, 큰 값을 담은 리스트를 생성하고 합침
def quick_sort(array):
    # array 요소가 하나 이하라면 정렬할 필요도 없고 걍 반환하면 됨
    if len(array) <= 1:
        return array
    
    # 맨 앞에 있는 것을 피봇으로 정함 내맘임
    pivot = array[0]
    
    # 피봇보다 작은 값들 모은 리스트
    left = [x for x in array if x < pivot]
    # 피봇과 동일한 값들 모은 리스트
    equal = [z for z in array if z == pivot]
    # 피봇보다 큰 값들을 모은 리스트
    right = [y for y in array if y > pivot]
    
    # 재귀 돌면서 리스트들 합치고 합치면 됩니다ㅣ아.ㅇㅇ
    return quick_sort(left) + equal + quick_sort(right)

for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    sorted_list = quick_sort(a)
    print(f'#{tc} {sorted_list[n//2]}')