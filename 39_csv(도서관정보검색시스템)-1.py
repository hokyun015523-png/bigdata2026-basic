# 0번 열 - 도서관 코드, 1번 열 - 도서관 병, 2번 열 - 주소, 3번 열 - 상세주소
# 4번 열 - 전화번호, 5번 열 - 팩스번호, 6번 열 - 홈페이지, 7번 열 - 개관 시간 
# 8번 열 - 휴관일

# CSV 라이브러리 불러오기
from csv import * #CSV라이브러리 안 모든 함수를 가져와라. 호출 시 함수명으로 호출 가능/ 만약 비슷한 함수가 있으면 충돌될 가능성 있음

file = open('library.csv', 'r')
read_file = reader(file) # csv안의 reader함수를 불러온다 -> flie객체 내용을 다 읽기

library_list = []
for line in read_file:
    library_list.append(line)
file.close()

library_lnfo = ['도서관코드', '도서관명', '상세주소', '펙스' ,'홈페이지', '개관시간', '휴무일']

while True:
    search_word = input('\n검색어 입력 (종료:0) : ')
    if search_word == '0':
        print('\n[도서관 정보 검색 시스템 종료]') # print('\n[도서관 정보 검색 시스템 종료]'); break ->이런식으로 해도 다음줄 코드로 됨
        break
    print(f'\n제공정보 --> {library_lnfo[2:]}')

    print_info = input('\n원하는 정보 입력 (예시:주소 휴관일) : ').split() # 공백을 기준으로 나눠서 저장
    print('-' * 70)
    print('\n[도서관 정보 검색 결과]')
    for line in library_list:
        if search_word in line[1]: # 찾는 단어가 line[1](도서관 명)에 포함되어 있니?
            #print(f'{line[1]} / {line[2]} / {line[4]}') # 도서관명 / 주소 / 전화번호 -->묹제 1번
            print (line[1], end=' | ')
            for i in print_info: # 예) 휴관일
                if i in library_lnfo:
                    print(line[library_lnfo.index(i)], end=' | ') #인덱스 번호를 추출 -->. index()
            print()
    print('-' * 70)