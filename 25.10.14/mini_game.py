class Character:
    def __init__(self, name, hp, mp, attack_power,STR, INT):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack_power = attack_power
        self.STR = STR
        self.INT = INT
    def attack(self, target):
        print(f"{self.name} 이/가 {target.name} 을/를 공격했다 ! (공격력 : {self.attack_power})")
        target.hp -= self.attack_power
        print(f"{target.name}의 남은 체력 : {target.hp}")
    def info(self):
        print(f"이름 : {self.name} | hp : {self.hp} | mp: {self.mp} | attack_power : {self.attack_power}")

class Warrior(Character):
    def info(self):
        print("직업 : 전사")
        super().info()
    def attack(self, target):
        damage = int(self.attack_power * self.STR * 0.12)
        print(f"{self.name} 이/가 {target.name} 을/를 강하게 공격했다 ! (공격력 : {damage})")
        target.hp -= damage
        print(f"{target.name}의 남은 체력 : {target.hp}")
class Mage(Character):
    def info(self):
        print("직업 : 마법사")
        super().info()
    def attack(self, target):
        damage = int(self.attack_power * self.INT * 0.12)
        print(f"{self.name} 이/가 {target.name} 을/를 마법으로 공격했다 ! (공격력 : {damage})")
        target.hp -= damage
        print(f"{target.name}의 남은 체력 : {target.hp}")


c1 = Character("바보",100,50,10,4,4)
w1 = Warrior("인병",100,50,10,10,4)
m1 = Mage("뇽",100,50,10,4,10)
c1.attack(w1)
w1.attack(c1)
m1.attack(w1)