# 타입 어노테이션(annotation)
# --> 파이썬은 자료형선언 없이 변수나 함수를 자유롭게 사용할 수있다는 특징이 있습니다
# --> 자료형을 파악하기 어려운 경우가 종종 발생하게된다
# --> 파이썬3.5버전 이상에서 사용가능
# --> 강제성이 없는 자료향에 관한 힌트를 알려준다. -->꼭 지킬 이유가 없다
# --? 코드 자체에도 영향을 미치지 않는다 --> 에러도 나지 않는다

#----------------------------------------------------------------------------------------
# ex 일반적으로 지금까지 공부한 파이썬 변수 정리
num = 1 # 정수 값을 받은 변
li = [1,2.3/4]
d = {'name':'푸바오', 'age':5}
print(num,li, d, sep='\n')
print(type(num), type[li], type(d), sep='\n')

print('=' * 50)
#-------------------------------------------------------------------
#ex) 어노테이션을 넣는 변수
num: int = 1 #  변수 이름은 num, 되도록 int형으로 해라
li: list = [1,2,3,4]
d: dict = {'name':'푸바오', 'age':5}
print(num, li, d, sep='\n')
print(type(num), type(li), type(d), sep='\n')

#----------------------------------------------------------------------------------------
#ex) 일반적인 함수 정의 방법
def add(a,b):
    return a+b

result = add(1,2) # 함수 호출
print(result) # 3.3000000000003
print(type(result)) # <class 'int'>

result2 = add(1.1,2.2) # 함수 호출
print(result2)
print(type(result2)) # <class 'float'>

result3 = add('안녕', '메롱') # 함수 호출
print(result3)
print(type(result3)) # <class 'str'>

result4 = add([1, 2],[3, 4])
print(result4)
print(type(result4)) # <class 'list'>

print('=' * 50)
#-----------------------------------------------
# ex) 어노테이션 적용한 함수 정의
#def 함수명(매개변수명:자료형) ->반환형의 자료형:
# 함수본체
def sub(a: int, b: int) -> int:
    return a - b

result= sub(20,10) #함수 호출
print(result)
print(type(result))

result2 = sub(20.2, 10.1) #함수 호출
print(result2)
print(type(result2))

result3 = add('안녕', '메롱') # 함수 호출
print(result3) # 에러
print(type(result3)) 