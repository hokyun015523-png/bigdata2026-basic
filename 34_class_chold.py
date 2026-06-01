# # 상속
# # -> 부모(슈퍼)클래스의 코드를 자식(서브) 클래스가 물려받는 것

# class Animal: #클래스 정의- 부모(슈퍼) 클래스
#     def __init__(self): # 생성자
#         self.height = 30   # 인스턴스 변수

#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# fubao = Animal() # 인스턴스(객체) 생성
# fubao.get_height() # 인스턴스 메서드 호출

# class Dog(Animal): # 자식(서브) 클래스 정의 class자식클래스명(부모클래스명):
#     pass

# class Cat(Animal):
#     pass

# mung = Dog()
# mung.get_height() # 상속 받은 인스턴스 메서드 호출

# yaong = Cat()
# yaong.get_height()

# print(fubao)
# print(mung)
# print(yaong)

# --------------------------------------------------------------------------------
# class Animal: #클래스 정의- 부모(슈퍼) 클래스
#     def __init__(self): # 생성자
#         self.height = 30   # 인스턴스 변수

#     def get_height(self): # 인스턴스 메서드
#         print(f'Animal {self.height}')

# class Dog(Animal):
#     def cry(self):
#         print('멍멍!')
    
# class Cat(Animal):
#     def run(self):
#          print('살곰살곰')

# fubao = Animal()
# mung = Dog()
# yaong = Cat()

# fubao.get_height()
# print('-' * 50)

# mung.get_height()
# mung.cry()
# print('-' * 50)

# yaong.get_height()
# yaong.run()

# --------------------------------------------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def holle(self):
#         print(f'안녕하세요! 저는{self.name}입니다.')

# class Child(Parent):
#     pass

# person1 = Parent('김슈퍼') #<__main__.Parent object at 0x00000177715B8E10>
# person1.holle()

# person2 = Child('김서브') #<__main__.Child object at 0x00000177715B98D0>
# person2.holle

# print(person1)
# print(person2)

# --------------------------------------------------------------------------

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def holle(self):
#         print(f'안녕하세요! 저는{self.name}입니다.')
# class Child(Parent):
#     def bye(self):
#         print(f'{self.name}은(는) 떠납니다')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브')

# person1.holle()
# print('-' * 50)

# person2.holle()
# person2.bye()

# --------------------------------------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def holle(self):
#         print(f'안녕하세요! 저는{self.name}입니다.')

# class Child(Parent):
#     def __init__(self, name, age): # 메서드 덮어쓰기(자식이 부모를 덮는다)
#         super().__init__(name)
#         self.age = age

#     def bye(self):
#         print(f'{self.age}살인 {self.name}은(는) 떠납니다')

# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.holle()
# print('-' * 50)

# person2.holle()
# person2.bye()

# # --------------------------------------------------------------------------
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def holle(self):
#         print(f'안녕하세요! 저는 {self.name}입니다.')

# class Child(Parent):
#     def __init__(self, name, age): # 메서드 덮어쓰기(자식이 부모를 덮는다)
#         super().__init__(name) #부모의 생성자를 호출
#         self.age = age

#     def bye(self):
#         super().holle() # 부모의 인스턴스 메서드 호출
#         print(f'{self.age}살인 {self.name}은(는) 떠납니다')


# person1 = Parent('김슈퍼')
# person2 = Child('김서브', 20)

# person1.holle()
# person2.bye()

# --------------------------------------------------------------------------
class Car: #부모 (슈퍼) 클래스
    max_oil = 50 # 클래스 변수 --> 최대 주유량

    def __init__(self, oil):
        self.oil = oil # 인스턴스 변수--> 현대 기름량

    def add_oil(self, oil):
        if oil <= 0: # 0이하는 주유를 진행하지 않는다.
            return #함수 종료 ( 아무것도 안적혀 있으면 그냥 함수 종료)
        self.oil += oil # oil만큼 기름 넣는다.
        if self.oil > self.max_oil: # -> 최대 주유량 보다 크다면 
            self.oil = Car.max_oil #->  현재 기름량을 최대 주유량으로 설정해 놓아 50 이상은 못하게
    
    def car_info(self):
        print(f'현재 주유 상태(기름량) : {self.oil}')
        
car1 = Car(20)
car1.car_info()
car1.add_oil(40)
car1.car_info()

class Hybrid(Car):
    max_battery = 30 # 최대 배터리 충전량 --> 클래스 변수

    def __init__(self, oil, battery):
        super().__init__(oil) # 부모의 생성자를 호출
        self.battery =  battery #인스턴스 변수

    def charge(self, battery): # 인스턴스 메서드 정의
        if battery <= 0:
            return #함수 종료
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery #최대 충전량으로 설정

    def hybrid_info(self):  # 인스턴스 메서드 정의
        super().car_info() # 부모의 메서드 호출
        print(f'현재 충전상태 :{self.battery}')

car2 = Hybrid(10,5) # 10은 oil의 값, 5는 battery의 값
car2.hybrid_info()
car2.add_oil(35)
car2.charge(40)
car2.hybrid_info()

