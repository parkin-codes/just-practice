# if 정수열에 관하여
a = int(input('5*6?'))
if a == 30:
    b = input('확신하시나요?')
    if '예' in b:
        print('정답입니다!')
    else:
        print('그걸 고민한다고?')
else:
    print('진짜 병신이세요?')