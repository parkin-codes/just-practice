class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("소리를 낸다")
    def info(self):
        print(f"이 동물의 이름은 {self.name}입니다.")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("멍멍")

class Cat(Animal):
    def sound(self):
        super().sound()
        print("야옹")

d = Dog("토리")
c = Cat("나비")

animals = [d, c]
for a in animals:
    a.sound()