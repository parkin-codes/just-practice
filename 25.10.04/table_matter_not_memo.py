전체사람수 = 100
memo = {}
리턴값 = 0
def 그래프(노드, 이전화살표):
    if 노드 == 0:
        global 리턴값
        리턴값 += 1
    for i in range(max(2,이전화살표),min(노드,10)+1):
        그래프(노드-i,i)
    return 리턴값
    
print(그래프(전체사람수,0))