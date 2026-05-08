# for 와 문자열
hello = '안녕하세요!'
for h in hello: # hello --> 문자열
    print(h) #  한 글자씩 들어간다.

print('-' * 50)

# for와 리스트
li = ['바르셀로나', '메시', '수아레스', '네이마르', '라마시아']
for i in li:
    print (i)

print('-' * 50)

# for와 딕셔너리
menu = {'김밥':3000, '라면':5000, '떡볶이':4000}
for m in menu:
    print(m) # key가 출력

for m in menu:
    print(menu[m]) # key(m)에 해당하는 값이 출력

for dic in menu.items():
    print(dic)

for k, v in menu. items():
    print(f'key:{k}, value:{v}')

print('-' * 50)

for i in range(100):
    print(i) # 0 ~ 99

print('-' * 50)

for i in range(1,31):
    print(i, end=' ')
    
print()
print('-' * 50)

for i in range(1, 31, 2):
    print(i, end=' ') # 홀수만

print()
print('-' * 50)

# 거꾸로 30 -> 1 (1씩 감소)
for i in range(30, 0, -1):
    print(i, end=' ')
    