numbers = list(range(1,11))

print("# 홀수만 추출하기")
print(list(filter(lambda x:x%2==1,numbers)))
print()

print("# 3 이상 7미만 추출하기")
print(list(filter(lambda x:3<=x<7,numbers)))
print()

print("# 제곱해서 50미만 추출하기")
print(list(filter(lambda x: x**2 <50,numbers)))