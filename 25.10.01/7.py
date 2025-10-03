def mul(*value):
    output = 1
    for i in value:
        output *= i
    return output

print(mul(10,5,7,9))