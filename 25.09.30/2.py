# 변수를 선언합니다.
example_dict = {
    "키1" : "값1",
    "키2" : "값2",
    "키3" : "값3",
}

# 딕셔너리의 items() 함수 결과 출력하기
print("# 딕셔너리의 item() 함수 결과 출력하기")
print("item():",example_dict.items())
print()

# for 반복문과 items() 함수 조합해서 사용하기
print('# 딕셔너리의 items() 함수와 반복문 조합하기')

for key, element in example_dict.items():
    print(f"dictionary[{key}] = {element}")