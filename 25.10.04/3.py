def 함수():
    print("함수에 진입했습니다")
    try:
        print("try구문에 진입했습니다")
        
        print("try구문이 끝났습니다.")
    except:
        print("except구문에 진입했습니다")
    finally:
        print("finallyt구문에 진입했습니다")
    print("함수가 끝났습니다")

함수()