import datetime
now=datetime.datetime.now()
a = input('password :')
if a == '0415':
    b=input('무엇을 알려드릴까요?')
if '메뉴' in b:
    print('제육볶음')
elif '시간' in b:
    print(f'현재 시각은 {now.hour}시 {now.minute}분 입니다.')
else:
    print('감사합니다')
if a != '0415':
    print('비밀번호가 틀렸습니다.')
    

