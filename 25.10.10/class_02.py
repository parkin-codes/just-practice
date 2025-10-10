class Gym:
    def __init__(self, name, age, program, sessions):
        self.name = name
        self.age = age
        self.program = program
        self.sessions = sessions
    def attend(self):
        if self.sessions == 0:
            print("이용권이 만료되었습니다.")
        elif self.sessions >= 1:
            self.sessions -= 1
            return self.sessions
    def extend(self, n):
        self.sessions += n
        return self.sessions
    def check_status(self):
        print(f"이름 :{self.name} 나이 :{self.age} 프로그램명 :{self.program} 이용권횟수 : {self.sessions}")

user_list=[
    Gym("박병인",27,"자유운동",29),
    Gym("김안녕",20,"PT",20),
    Gym("이하세",29,"필라테스",19),
    Gym("문요",24,"자유운동",25),
    Gym("안반갑",25,"PT",3)
]



for i in user_list:
    i.check_status()
