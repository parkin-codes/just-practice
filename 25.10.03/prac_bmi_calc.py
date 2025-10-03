#스트림 연결
with open("human_list.txt","r") as file:
    # 한 줄씩 반복
    for i in file:
        name, height, weight = i.strip().split(",")
        height = int(height)
        weight = int(weight)
        #bmi 계산식
        bmi = weight / (height/100)**2
        # bmi 판단
        if bmi >= 25:
            result = "과체중"
        elif bmi >= 18:
            result = "정상체중"
        else:
            result = "저체중"
        # 출력합니다.
        print("\n".join([
            f"이름 : {name}",
            f"키 : {height}",
            f"몸무게 : {weight}",
            f"bmi : {bmi:.1f}",
            f"결과 : {result}\n"]))