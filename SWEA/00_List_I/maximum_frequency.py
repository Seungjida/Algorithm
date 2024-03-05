T = int(input())

for test_count in range(T):
    test_number = int(input())
    
    grade_student_num = {}
    grades = map(int, input().split())
    for grade in grades:
        if grade in grade_student_num.keys():
            grade_student_num[grade] += 1
        else:
            grade_student_num[grade] = 1

    desc_by_student_num = sorted(grade_student_num.items(), key = lambda x: x[1], reverse = True)
    print(f'#{test_number} {desc_by_student_num[0][0]}')