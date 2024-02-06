import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for test_case in range(1, T+1):
    # 알파벳이 몇 개씩 들어간지 저장할 딕셔너리 생성 및 0으로 초기화
    # 알파벳을 하나씩 넣기 보다는 유니코드 이용하여 for문 돌려 만들고, 또 대소문자 구분한다는 가정하에 만듦
    alpha = {}
    for i in range(ord('A'), ord('Z')+1):
        alpha[chr(i)] = 0
    for j in range(ord('a'), ord('z')+1):
        alpha[chr(j)] = 0
    
    # str1에 같은 알파벳이 나와도 어차피 하나의 알파벳으로 치니까 set()을 이용해 중복 알파벳 걸러냄
    str1 = set(input())
    str2 = input()
    
    # str1의 알파벳을 하나씩 뽑고
    for a in str1:
        # str2의 알파벳들과 비교
        for target in str2:
            # 같으면 해당 알파벳을 키로 가지는 값을 ++
            if target == a:
                alpha[target] += 1
    # 가장 큰 값을 구한다
    max_count = max(alpha.values())
    print(f'#{test_case} {max_count}')