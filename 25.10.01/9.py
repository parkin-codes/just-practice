a = 10
b = [1, 2, 3, 4]

def f():
    global a,b # 이걸 쓰면 바깥 영역에도 영향을 주게됨.
               # 원래는 f() 내부에서만 영향을 주는 애들이지만 global을 쓰게되면 바깥 영역까지
               # 손을 대겠다라는 위험한 의미.
    a = 20
    b = [5, 6, 7, 8]
    print(a)
    print(b)

f()
print(a)
print(b)