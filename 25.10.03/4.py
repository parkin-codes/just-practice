with open("data.txt","r") as file:
    if file != "":
        print(file.read().strip().split("\n"))

문자열 = input("> 데이터를 입력해주세요")

with open("data.txt","a") as file:
    file.write(문자열.strip() + "\n")