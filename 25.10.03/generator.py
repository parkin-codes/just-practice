범위 = range(1, 100+1)
제너레이터표현식 = (
    x ** 2
    for x in 범위
)
print(next(제너레이터표현식))
print(next(제너레이터표현식))
print(next(제너레이터표현식))
print(next(제너레이터표현식))
print(next(제너레이터표현식))

def 제너레이터함수():
    for i in 범위:
        yield i * i
제너레이터 = 제너레이터함수()
for 요소 in 제너레이터:
    print(요소)