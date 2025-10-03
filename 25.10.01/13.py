memo = {
    1 : 1,
    2 : 1,
}
def fibo(n):
    if n in memo:
        return memo[n]
    else:
        temp = fibo(n-1) + fibo(n-2)
        memo[n] = temp
        return temp
    

print(fibo(100))
print(memo)