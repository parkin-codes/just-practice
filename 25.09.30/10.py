scores = {
    "철수": {"국어": 85, "수학": 90},
    "영희": {"국어": 92, "수학": 88},
    "민수": {"국어": 78, "수학": 95}
}
total = 0

for i, value in enumerate(scores):
    print(f"{i + 1}번째 학생 : {value}")
    for key, value_1 in scores[value].items():
       print(f" {key} : {value_1}점")
    a =list(scores[value].values())
    print(f" 평균 :{sum(a)/len(a):.1f}점")
