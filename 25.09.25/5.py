students = [
    {"name": "민수", "score": 92},
    {"name": "영희", "score": 76},
    {"name": "철수", "score": 88}
]
for i in students:
    if i["score"] > 80 :
        print(f'{i["name"]}의 점수는 {i["score"]}점이고, 합격입니다.')
    else:
        print(f'{i["name"]}의 점수는 {i["score"]}점이고, 불합격입니다.')