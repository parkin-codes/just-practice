전체사람수 = 6
count =0
def 그래프(노드, 화살표):
    if 노드 == 0:
        global count
        count += 1
    for i in range(max(2,화살표),min(10,노드)+1):
        그래프(노드-i, i)
    return count
print(그래프(전체사람수,0))