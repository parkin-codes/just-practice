파일 = open("human.txt","r")

for 한줄 in 파일:
    이름,몸무게,키 = 한줄.strip().split(",")
    if not 몸무게.isdigit():
        continue
    몸무게 = int(몸무게)
    키 = int(키)

    bmi = 몸무게 / (키 /100)**2 
    결과 = ""
    if 25 <= bmi:
        결과 = "과체중"
    elif 18.5 <= bmi:
        결과 = "정상체중"
    else :
        결과 = "저체중"
    print("\n".join([
        f"이름 : {이름}",
        f"몸무게 : {몸무게}",
        f"키 : {키}",
        f"bmi : {bmi:.1f}",
        f"결과 : {결과}", "\n"
           ]))
파일.close()
