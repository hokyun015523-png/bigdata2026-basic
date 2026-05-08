# 주석
# 변수 만들기
# <형식>
# 변수명 = 값
hello = '안녕 파이썬' #작은 따움표, 큰 따옴표 다 사용 가능
print(hello)
#변수명은 숫자로 시작할 수 없다, 특수문자도 사용 못함! 5hello = 'aaa'

# import = 'a' # 예약어도 변수명으로 사용할 수 없다!
# ctrl 누르고 / --> 한번에 주석 처리, 해제

# 예약어 확인
import keyword
print(keyword.kwlist)

print()  #빈 줄 의미 

# 본인의 이름과 나이를 변수에 저장한 후 출력 (67P)
name = '장호균'
age = 25
print(name, age)
print(name, age, sep='::', end='^^')
print(name, age, sep='::')

print()

# 자료형 
# 기본 자료형 : int(정수), float(실수), bool(참/거짓, 논리, 불), str(문자열)
# 컬렉션 자료형 : 덩어리, 배열 같은 것 list(리스트), dict(딕셔너리), tuple(듀플), set(세트)
num = 100
print(num)
print(type(num)) #type은 자료형을 볼 수 있다

num = 95.5
print(num)
print(type(num))

name = '홍길동'
print(name)
print(type(name))

result = True # True --> 참, False--> 거짓
print(result)
print(type(result))
