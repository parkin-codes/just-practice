전체사람수 = 100
memo = {}
def 그래프(노드, 화살표):
    count = 0
    if (노드, 화살표) in memo:
        return memo[(노드,화살표)]
    if 노드 == 0:
        count += 1
    else:
        for i in range(max(2,화살표),min(10,노드)+1):
            count += 그래프(노드-i, i)
    return count
print(그래프(전체사람수,0))