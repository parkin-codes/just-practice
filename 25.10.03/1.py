memo = {1:1}

def factorial(n):
    if n in memo:
        return memo[n]
    else:
        value = n * factorial(n-1)
        memo [n] = value
        return value
    
print(factorial(30))