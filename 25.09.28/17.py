import random
target = random.randint(1,100)
count = 0
while True:
    input_a = input('1~100 사이 숫자를 입력하세요')
    number = int(input_a)
    count += 1
    if number > target:
        print('더 작은 수를 입력하세요')
    elif number < target:
        print('더 큰 수를 입력하세요')
    elif number == target:
        print(f'정답입니다! 시도 횟수 : {count}')
        break

