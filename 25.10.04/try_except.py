입력리스트 = ["52","273","32.1","103","하이"]
출력리스트 = []
for i in 입력리스트:
    try:
        출력리스트.append(float(i))
    except :
        pass

print(출력리스트)