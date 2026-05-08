# 리스트 자료형 (빈 리스트 생성)
li = []
print(li)

li2 = list()
print(li2)

# append() --> 맨 뒤에 값(하나) 추가
li.append('바르셀로나')
print(li)

li.append('메시')
print(li)

li.append('수아레스')
print(li)

li.append('네이마르')
li.append('라마시아')
print(li)

# 인덱싱 --> 0 부터 출력. -1 맨 끝 값을 의미함
print(li[0]) # 바르셀로나
print(li[3]) # 네이마르
print(li[-1]) # 라마시아

#  슬라이싱
#  <형식>
# 리스트명 [시작 인덱스번호 :끝 인덱스번호+1:증감값]
# 증감값은 보통 생략 (1씩 증가가 대부분)
print(li[1:4])
print(li[1:]) # 끝 번호 생략 가능 (끝까지)
print(li[:3]) # 첫 번호 생략 가능 (처음부터)
print(li[:]) # 인덱스 번호 모두 (전체)
print(li[::-1]) # 반전 (거꾸로)

# list 값(요쇼) 변경
li[3] = '이니에스타' # 인덱스번호 3번 자리에 '이니에스타'로 수정
print(li)

# 튜플 자료형 --> 고정값, 수정, 추가, 삭제 불가
print()
