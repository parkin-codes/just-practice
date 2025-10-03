limit = 10000
i = 1
sum_value = 0
while sum_value <= 10000:
    sum_value += i
    i += 1
print(f'{i-1}를 더할때 {limit}을 넘으며, 그떄의 값은 {sum_value}입니다.') 