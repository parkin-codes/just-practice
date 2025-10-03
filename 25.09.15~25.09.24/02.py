a = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for b in a:
    if b%2==0:
        print(b,'는 짝수입니다.')
    if b%2==1:
        print(b,'는 홀수입니다.')

for b in a:
    if b<10:
        print(b,'는 1자릿수 입니다.')
    elif b<100:
        print(b,'는 2자릿수 입니다.')
    else:
        print(b,'는 3자릿수 입니다.')