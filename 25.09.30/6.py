# 변수를 선언합니다.
number = int(input('정수를 입력하세요 :'))

# if 조건문으로 홀수 짝수를 구분합니다.
if number % 2 == 0 :
    print(f'입력한 문자열은 {number}입니다.\n{number}는(은) 짝수입니다.')
else:
    print(f'입력한 문자열은 {number}입니다.\n{number}는(은) 홀수입니다.')