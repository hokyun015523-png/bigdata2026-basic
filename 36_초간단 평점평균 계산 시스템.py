# 함수 정의
def graduate():
    """졸업 요건 확인해주는 함수"""
    tot_semester = int(input('\n총 등록 학기수 입력 : '))
    if tot_semester >= 8:
        print('졸업학기 충족 완료')
    else:
        print(f'{8-tot_semester}학기 부족')
    
    tot_credit = int(input('\n수강 완료 학점수 입력 : '))
    if tot_credit >= 120:
        print('졸업학점 충족 완료')
    else:
        print(f'{120-tot_credit}학점 부족')

    tot_grade = float(input('\n총 평균평점 입력 : '))
    if tot_grade >= 2.5:
        print('졸업 평균평점 충족 완료\n')
    else:
        print(f'{2.5-tot_grade:.2f} 평균평점 낮음\n')

# 함수 정의
def avg_grade():
    total = 0
    result = 0
    for i in course:
        if i[2] == 'A':
            total += i[1]
            result += i[1] * 4.5
        elif i[2] == 'B':
            total += i[1]
            result += i[1] * 3.5
        elif i[2] == 'C':
            total += i[1]
            result += i[1] * 2.5
        elif i[2] == 'F':
            total += i[1]
    return result / total 


# 함수 정의
def subject():
    """수강 강좌정보를 입력하는 함수"""
    while True:
        title = input('과목명(0은 종료) : ')
        if title == '0':
            break
        credit = int(input('학점 수 : '))
        grade = input('취득학점(A,B,C,F) : ')
        course.append([title, credit, grade])

course = []
while True:
    choice = int(input('1.수강 강좌정보 입력 2.평균평점 확인 3.졸업여건 확인 0.종료 : '))
    if choice < 0 or choice > 3:
        print('없는 번호!')
        continue
    elif choice == 1:
        print('\n< 수강 강좌정보 입력 > ')   
        subject() # 함수 호출
        print('< 수강 강좌정보 입력 종료 >\n')     
    elif choice == 2:
        print('\n< 수강 강좌 목록 >')
        print('과목명\t학점수\t학점')
        print('-' * 20)
        gpa = avg_grade()
        for c in course:
            print(f'{c[0]}\t{c[1]}\t{c[2]}')# 함수 호출
        print(f'\n평균평점 : {gpa:.2f}\n')
    elif choice == 3:
        graduate() # 함수 호출
    elif choice == 0:
        print('초간단 평점평균 계산 시스템 종료!')
        break