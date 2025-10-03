a = 10
b = [1, 2, 3, 4]

def f():
    global a,b
    print(a)
    print(b)
    print()
    a = 20
    b = [5, 6, 7, 8]
    print(a)
    print(b)
    print()

f()
print(a)
print(b)