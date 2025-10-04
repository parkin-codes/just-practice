전체사람수 = 6
memo = {}

def 그래프(노드, 이전화살표):
    if (노드,이전화살표) in memo:
        return memo[(노드, 이전화살표)]
    리턴값 = 0
    if 노드 == 0:
         리턴값 += 1
    else:
        for i in range(max(2,이전화살표),min(노드 +1,10)):
           리턴값 += 그래프(노드-i,i)
    return 리턴값
    
print(그래프(전체사람수,0))