# # 교재113P

# # 구구단 2단
# for i in range(1,10):
#     print(f'2 X {i} = {2 * i}') #  2 X 1 = 2

# # 단을 입력받아 구구단 추력
# num = int(input('단 입력 : '))
# for i in range(1,10):
#     print(f'{num} X {i} = {num * i}')

# # 구구단 전체 출력
# # 단 --> 2단 ~9단-->dna
# # 곱해지는 수 --> 1 ~ 9 --> i
# for dna in range(2, 10):
#     print(f'----{dan}단----')
#     for i in range (1, 10):
#         print(f'{dan} X {i} = {dan * i}')


# 중첩 for 이용 - 김밥 배합 출력
main = ['베이컨', '크래미']
side = ['당근', '오이']
x = 1
for m in main:
    for s in side:
        print(f'{x} : {m} + {s} + 계란')
        x += 1
