# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 시간/시간을 구합니다.
now = datetime.datetime.now()

# 출력합니다.
if now.hour >= 12:
    print(f'현재 시각은 오후 {now.hour}시 {now.minute}분 입니다.')
if now.hour < 12:
    print(f'현재 시각은 오전 {now.hour}시 {now.minute}분 입니다.')
