students = [
    {"name": "철수", "scores": {"국어": 80, "영어": 75, "수학": 90}},
    {"name": "영희", "scores": {"국어": 95, "영어": 85, "수학": 100}},
    {"name": "민수", "scores": {"국어": 70, "영어": 65, "수학": 80}}
]

for student in students:
    print(f"[{student["name"]}]의 성적표")
    for key,value in student["scores"].items():
        print(f" {key} : {value}점")
    score = student["scores"].values()
    sum_a = sum(score)
    len_a = len(score)
    print(f" 총점 :{sum_a}점, 평균 : {sum_a / len_a:.1f}점")