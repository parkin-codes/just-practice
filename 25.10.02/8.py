def power(숫자):
    return 숫자 * 10 

def is_odd(숫자):
    if 숫자 % 2 == 1:
        return True

def my_map(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        output.append(콜백함수(요소))
    return output

def my_filter(콜백함수, 리스트):
    output = []
    for 요소 in 리스트:
        if 콜백함수(요소):
            output.append(요소)
    return output

A = [1,2,3,4,5]

print(my_map(power,A))
print(my_filter(is_odd,A))


print(list(map(power,A)))
print(list(filter(is_odd,A)))