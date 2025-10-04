전체사람수 = 100
memo = {}
def 그래프 (노드,이전화살표):
    if (노드,이전화살표) in memo:
        return memo[(노드, 이전화살표)]
    리턴값 = 0
    if 노드 == 0:
        리턴값 += 1
    else:
        for i in range(max(2,이전화살표),min(10,노드)+1):
           리턴값 += 그래프(노드 - i, i)
    return 리턴값
import time
이전시간 = time.time()
print(그래프(전체사람수, 0))
이후시간 = time.time()
print(이후시간-이전시간)