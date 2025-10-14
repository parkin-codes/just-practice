class Student:
    __count = 0
    student_list=[]
    student_dict={}
    __next_id= 1
    def __init__(self, name, grade):
        self.id = Student.__next_id      
        self.name = name
        self.grade = grade
        Student.student_list.append(self)
        Student.student_dict[self.id]=Student.info()
        Student.__count += 1
        Student.__next_id += 1
    def info(self):
        return f"ID : {self.id} | 이름 : {self.name} | 학년 : {self.grade}"
    @classmethod
    def how_many(cls):
        return cls.__count
    @classmethod
    def show_all(cls):
        print("전체 학생 목록")
        for student in Student.student_list:
            student.info()

s1 = Student("철수",1)
s2 = Student("영희",2)
s3 = Student("감자",3)

s1.search()