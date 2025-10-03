# 스트림 연결
file = open("text.txt","r")
# 스트림을 통해 데이터 통신
문자열 = file.read()
print(문자열) 
# 스트림 해제
file.close()

# whit ... as :
with open("text.txt","r") as file:
    문자열 = file.read()
    print(문자열) 