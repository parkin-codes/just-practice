# 학생 리스트를 선언합니다.
students = [
    {'name': '윤명성', 'korean': 87, 'math': 98, 'zzz': 88, 'science': 95},
    {'name': '연하진', 'korean': 92, 'math': 98, 'zzz': 96, 'science': 98},
    {'name': '구지연', 'korean': 76, 'math': 96, 'zzz': 94, 'science': 90},
    {'name': '나서영', 'korean': 98, 'math': 92, 'zzz': 96, 'science': 92},
    {'name': '윤이나', 'korean': 95, 'math': 98, 'zzz': 98, 'science': 98},
    {'name': '김재훈', 'korean': 64, 'math': 88, 'zzz': 92, 'science': 92}
]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    #점수의 총합과 평균을 구합니다.
    score_sum = student["korean"]+student["math"]+student["english"]+student["science"]
    score_aver = score_sum/4
    print(student["name"],score_sum,score_aver, sep="\t")