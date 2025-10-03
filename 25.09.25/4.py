student = {
    "name": "민수",
    "age": 17,
    "scores": {
        "math": 92,
        "english": 85,
        "science": 88
    },
    "hobbies": ["축구", "게임", "독서"]
}

print(f'학생 {student["name"]}({student["age"]})세의 성적:')
for key in student:
    if type(student[key]) is dict:
        print(f"수학 :{student["scores"]["math"]}, 영어:{student["scores"]["english"]}, 과학 :{student["scores"]["science"]}")
    elif type(student[key]) is list:
        print(f'취미 :{student["hobbies"]}')