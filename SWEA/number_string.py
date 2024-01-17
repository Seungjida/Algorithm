T = int(input())

for test_count in range(1, T+1):
    N, M = map(int, input().split())

    N_number_list = list(map(int, input().split()))
    M_number_list = list(map(int, input().split()))

    len_distance = abs(N-M)
    smaller_len = min(N,M)
    bigger_len = max(N,M)

    facing_max = 0
    for attempts in range(len_distance + 1):
        facing_tmp = 0
        for index in range(smaller_len):
            if N == bigger_len:
                facing_tmp += (N_number_list[index + attempts] * M_number_list[index])
            else:
                facing_tmp += (N_number_list[index] * M_number_list[index + attempts])

        if facing_max < facing_tmp:
            facing_max = facing_tmp

    print(f'#{test_count} {facing_max}')