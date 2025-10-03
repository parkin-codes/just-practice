ops = {
    1: ("더하기", lambda x, y: x + y),
    2: ("빼기",   lambda x, y: x - y),
    3: ("곱하기", lambda x, y: x * y),
    4: ("나누기", lambda x, y: x / y if y != 0 else "0으로 나눌 수 없습니다.")
}

print("=== 계산기 ===")
for k, v in ops.items():
    print(f"{k}. {v[0]}")
print("0. 종료")

while True:
    try:
        number = int(input('메뉴를 선택하세요: '))
    except ValueError:
        print("숫자만 입력하세요!")
        continue

    if number == 0:
        print('프로그램을 종료합니다')
        break
    elif number in ops:
        try:
            b = int(input('첫 번째 숫자: '))
            c = int(input('두 번째 숫자: '))
            result = ops[number][1](b, c)
            print('결과:', result)
        except ValueError:
            print("정수만 입력하세요!")
    else:
        print('잘못된 선택입니다.')
