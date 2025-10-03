import random
# 텍스트를 생성합니니다.
with open("human_list.txt","w") as file:
    for i in range(100):
        name_sheet = "가나다라마바사아자차카타파하"
        name = random.choice(name_sheet) + random.choice(name_sheet)
        height = random.randrange(140,200)
        weight = random.randrange(40,120)
        file.write(f"{name},{height},{weight}\n")