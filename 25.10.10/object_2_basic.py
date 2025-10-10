# 학생 리스트를 선언합니다.
def create_name(name,korean,math,science,english):
    return {"name":name,"korean":korean,"math":math,"science":science,"english":english}
def score_sum(student):
    return student["korean"]+student["math"]+student["science"]+student["english"]
def score_aver(student):
    return score_sum(student)/4
students = [
    create_name("윤명성",87,98,88,99),   
    create_name("연하진",92,98,96,70),
    create_name("구지연",76,96,94,80),
    create_name("나서영",98,92,96,86),
    create_name("윤이나",95,98,98,91),
    create_name("김재훈",64,88,92,94),
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")


for student in students:
    #점수의 총합과 평균을 구합니다.
    print(student["name"],score_sum(student),score_aver(student), sep="\t")