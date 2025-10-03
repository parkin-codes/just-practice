students = [
    {"name": "민수", "scores": {"math": 92, "english": 85, "science": 88}},
    {"name": "영희", "scores": {"math": 76, "english": 95, "science": 80}},
    {"name": "철수", "scores": {"math": 88, "english": 72, "science": 60}}
]

#출력하기
for i in students:
    print(f'[{i["name"]}의 성적표]')
    for key in i:
        if isinstance(i[key],dict):
            print(f"수학 : {i[key]['math']}점 영어 : {i[key]['english']}점 과학 : {i[key]['science']}점")
            total = 0
            total = i[key]['math'] + i[key]['english'] + i[key]['science']
            aver = total / 3
            if aver >= 90:
                print(f'(총점 : {total}점, 평균:{aver:.1f} -> 등급 A')
            elif aver >= 80 :
                print(f'(총점 : {total}점, 평균:{aver:.1f} -> 등급 B')
            elif aver >= 70 :
                print(f'(총점 : {total}점, 평균:{aver:.1f} -> 등급 C')
            elif aver > 60 :
                print(f'(총점 : {total}점, 평균:{aver:.1f} -> 등급 F')