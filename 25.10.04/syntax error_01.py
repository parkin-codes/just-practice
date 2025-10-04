while True:
    입력 = input("정수를 입력하세요")

    try :
        숫자 = int(입력)
        print(숫자)
        break
    except:
        print("정수를 입력하지 않았습니다")