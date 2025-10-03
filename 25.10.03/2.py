def square(x):
    return x**2

def is_odd(x):
    return x%2 == 1

a = [1,2,3,4,5]

print(list(map(lambda x:x**2,a)))
print(list(filter(lambda x:x%2==1,a)))