class GymUser:
    gym_name = "파이썬 휘트니스"
    def __init__(self, name, program, sessions):
        self.name = name
        self.program = program
        self.sessions = sessions
    def attend(self):
        if self.sessions >= 1:
            self.sessions -= 1
            print(f"이용권 1회 차감. 남은 이용권:{self.sessions}회")
        else:
            print(f"이용권이 모두 만료되었습니다!")

    def extend(self, n):
        self.sessions + n
        print(f"이용권 {n}회 추가 완료! 남은 횟수 : {self.sessions}회")
    def check_status(self):
        print(f"이름 : {self.name} | 프로그램 : {self.program} | 남은 이용권 : {self.sessions}회")
    def __str__(self):
        return (f"{self.name}님 ( 프로그램 : {self.program}, 남은 이용권 : {self.sessions}회 )")

user_list = [
    GymUser("박병인","자유운동",14),
    GymUser("김바보","PT",8),
    GymUser("이천재","필라테스",9),
    GymUser("강보통","PT",0)
]

for i in user_list:
    i.check_status()
    GymUser.attend(i)
    print(i)
    print("-"*50)

