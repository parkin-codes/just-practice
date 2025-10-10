class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return print(f"안녕하세요. 제 이름은{self.name}이고 나이는{self.age}살 입니다.")
    
students_list = [
    {"name":"이태민","age":37},
    {"name":"김치영","age":35},
    {"name":"강문식","age":29},
    {"name":"문종철","age":31},
    {"name":"박병인","age":27}
]

def make_students():
    name_age = []
    for i in students_list:
        student = Student(i["name"],i["age"])
        name_age.append(student)
    return name_age

students = make_students()

for j in students:
    j.introduce()