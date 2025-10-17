import random
print("#random 모듈")
a = [1,2,3,4,5]
# random() : 0.0 <= x < 1.0 사이의 float를 리턴합니다.
print("- random() :", float(random.random()))

# uniform(min,max) : 지정한 범위 사이의 float를 리턴합니다.
print("- uniform(10,20) :", random.uniform(10,20))

# randrange() : 지정한 범위의 int를 리턴합니다.
# - randrange(max) : 0 - max 사이 값을 리턴합니다.
# - randrange(mix, max) : min 부터 max 사이 값을 리턴합니다.
print("- randrange(10) :", random.randrange(10))

# choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice(a) :", random.choice(a))

# shuffle(list) : 리스트의 요소들을 랜덤하게 섞습니다.
print("- suffle(a) :", random.shuffle(a))

# sample(list, k=<숫자>) : 리스트의 요소중 k개를 뽑습니다.
print("- sample(a),k=2) :", random.sample(a,k=2))