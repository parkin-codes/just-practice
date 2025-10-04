전체사람수 = 100
count = 0
def 그래프 (노드,이전화살표):
    if 노드 == 0:
        global count
        count += 1
    for i in range(max(2,이전화살표),min(10,노드)+1):
        그래프(노드 - i, i)
    return count
import time
이전시간 = time.time()
print(그래프(전체사람수, 0))
이후시간 = time.time()
print(이후시간-이전시간)