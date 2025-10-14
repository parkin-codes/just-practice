class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("소리를 낸다")

    def info(self):
        print(f"이 동물의 이름은 {self.name} 입니다.")


class Dog(Animal):   # 상속
    def sound(self): # 오버라이딩
        print("멍멍!")


class Cat(Animal):   # 상속
    def sound(self): # 오버라이딩
        print("야옹~")


# 사용
d = Dog("바둑이")
c = Cat("나비")

d.info()   # 부모 메서드
d.sound()  # Dog의 오버라이딩 메서드

c.info()   # 부모 메서드
c.sound()  # Cat의 오버라이딩 메서드

# 다형성 예시
animals = [d, c]
for a in animals:
    a.sound()