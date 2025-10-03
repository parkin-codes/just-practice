print("=== 계산기 ===")
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')
print('0. 종료')
while True:
    input_a = input('메뉴를 선택하세요')
    number = int(input_a)
    if number == 1:
        input_b = int(input('첫 번쨰 숫자 : '))
        input_c = int(input('두 번쨰 숫자 : '))
        print('결과 :',input_b + input_c)
    elif number == 2:
        input_b = int(input('첫 번쨰 숫자 : '))
        input_c = int(input('두 번쨰 숫자 : '))
        print('결과 :',input_b - input_c)
    elif number == 3:
        input_b = int(input('첫 번쨰 숫자 : '))
        input_c = int(input('두 번쨰 숫자 : '))
        print('결과 :',input_b * input_c)
    elif number == 4:
        input_b = int(input('첫 번쨰 숫자 : '))
        input_c = int(input('두 번쨰 숫자 : '))
        print('결과 :',input_b / input_c)
    elif number == 0:
        print('프로그램을 종료합니다')
        break
    else:
        print('잘못된 접근입니다.')