students = [
    {"name": "민수", "score": 92},
    {"name": "영희", "score": 76},
    {"name": "철수", "score": 88},
    {"name": "지민", "score": 65},
    {"name": "수현", "score": 54}
]

for i in students:
    if i["score"] >= 90:
        print(f'{i["name"]}의 점수는 {i["score"]}점 이고, 등급은 A 입니다.')
    elif i["score"] >= 80:
        print(f'{i["name"]}의 점수는 {i["score"]}점 이고, 등급은 B 입니다.')
    elif i["score"] >= 70:
        print(f'{i["name"]}의 점수는 {i["score"]}점 이고, 등급은 C 입니다.')
    elif i["score"] >= 60:
        print(f'{i["name"]}의 점수는 {i["score"]}점 이고, 등급은 D 입니다.')
    else :   
        print(f'{i["name"]}의 점수는 {i["score"]}점 이고, 등급은 F 입니다.')