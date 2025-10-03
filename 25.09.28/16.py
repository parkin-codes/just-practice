a = []
while True:
    input_a=input("정수를 입력하세용 :")
    number=int(input_a)
    if number == 0:
        break
    a.append(number)
sum_a = sum(a)
aver_a = sum(a) / len(a)
print('합계 :',sum_a)
print('평균 :',aver_a)