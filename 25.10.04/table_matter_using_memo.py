전체사람수 = 100
memo = {
   #"함수의 매개변수" : "리턴값"
} 
def 그래프(노드, 이전화살표에적힌숫자):
    if (노드, 이전화살표에적힌숫자) in memo:
        return memo[(노드, 이전화살표에적힌숫자)]
    리턴값 = 0
    if 노드 == 0 :
        리턴값 += 1
    else:
        for i in range(max(2,이전화살표에적힌숫자), min(10,노드)+1):
            리턴값 += 그래프(노드 - i, i)
    return 리턴값
print(memo)
print(그래프(전체사람수,0))