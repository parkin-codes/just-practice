import datetime
now = datetime.datetime.now()
a = input('입력 :')
if a in('안녕','안녕하세요'):
    print('안녕하세요!')
elif a in('지금 몇시야?','시간'):
    print(f'현재시각은{now.hour}시{now.minute}분 입니다.')
else:
    print('잘 지내?')