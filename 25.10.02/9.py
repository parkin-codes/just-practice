# 1. 이름을 입력받아 인사하기
def greet(name):
    print(f'"안녕하세요, {name}님!"')
greet("병인")


# 2. 제곱 계산
def square(num):
    a = num**2
    return a
print(square(10))

# 3. 섭씨 → 화씨 변환
def c_to_f(c):
    return c *9/5 + 32
print(f"화씨 : {c_to_f(36)}도")


# 4. 짝수 / 홀수 판별
def check_even_odd(n):
    if n % 2 == 0:
        return "짝수"
    else:
        return "홀수"
print(check_even_odd(3))


# 5. 학점 계산
def grade(score):
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else :
        return "F"
print(grade(76))


# 6. 리스트 합 구하기
def list_sum(numbers):
    output = 0
    for i in numbers:
        output += i
    return output
print(list_sum([1,4,5,2,3,4,1,5,5,6,7]))


# 7. 문자열 모음 개수 세기
def count_vowels(word):
    count = 0
    for i in word:
        if i in "aeiou":
            count += 1
    return count
print(count_vowels("Pneumonoultramicroscopicsilicovolcanoconiosis"))


# 8. 사칙연산 결과 반환 (합, 차, 곱, 나눗셈)
def calc(a, b):
    덧셈 = a + b
    뺄셈 = a - b
    곱셈 = a * b
    나눗셈 = a / b
    return 덧셈,뺄셈,곱셈,나눗셈
print(calc(10,5))

# 9. BMI 계산 & 해석
def bmi(height, weight):
    height_cm = height / 100
    a = weight / height_cm **2
    if a >= 25.0:
        return "과체중"
    elif a >= 18.5:
        return "정상"
    elif a < 18.5:
        return "저체중"
print(bmi(171,70))
