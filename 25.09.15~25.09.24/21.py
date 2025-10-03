# 입력을 받습니다.
a = input('숫자를 입력하세요')

# 마지막 숫자를 추출
num_a = a[-1]

# 추출한 숫자를 정수열로 변환
int_a = int(num_a)

# 짝수 확인
if int_a == 0 \
    or int_a == 2 \
    or int_a == 4 \
    or int_a == 6 \
    or int_a == 8:
    print('짝수입니다.')

# 홀수 확인
if int_a == 1 \
    or int_a == 3 \
    or int_a == 5 \
    or int_a == 7 \
    or int_a == 9:
    print('홀수입니다.')
    