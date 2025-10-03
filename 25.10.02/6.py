def power(숫자):
    return 숫자 ** 2

A = [1, 2, 3, 4, 5]
이터레이터 = map(power, A)
print(list(이터레이터))

print([
    숫자 **2
    for 숫자 in range(1, 5+1)
]
)
