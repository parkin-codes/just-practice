import os

# 기본 정보를 몇 개 출력해봅시다.
print("현재 운영체제:",os.name)
print("현재 폴더:",os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

# 폴더를 만들고 제거합니다.
os.mkdir("hello")
os.rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

# 파일을 제거합니다.
os.remove("new.txt")

# 시스템 명령어 실행
os.system("ls")

