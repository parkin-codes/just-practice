class Student:
    count = 0
    next_id = 1
    student_list = []
    student_dict = {}
    def __init__ (self, name, grade):
        self.id = Student.next_id
        self.name = name
        self.grade = grade
        Student.count += 1
        Student.next_id += 1
        Student.student_list.append(self)
        Student.student_dict[self.id]=self
    def info(self):
        print(f"ID : {self.id} | 이름 : {self.name} | 학년 : {self.grade}")
    @classmethod
    def how_many(cls):
        print(f"총 학생수 : {cls.count}")
    @classmethod
    def show_all(cls):
        print("======== 전체 학생 명단 ========")
        for student in cls.student_list:
            student.info()
            print("-"*30)
    @classmethod
    def search_by_name(cls, name):
        for student in cls.student_list:
            if student.name == name:
                student.info()
                return
        print("해당 이름의 학생은 존재하지 않습니다.")
            


s1=Student("철수",3)
s2=Student("영희",1)
s3=Student("미애",2)
s4=Student("희애",4)
s5=Student("애순",1)

Student.show_all()
Student.search_by_name("철수")
Student.student_dict(1) 