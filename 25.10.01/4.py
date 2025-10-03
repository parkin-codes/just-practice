def print_n_times(value,n=2):
    #n번 반복합니다.
    for i in range(n):
        print(value)
#함수를 호출합니다.
print_n_times("안녕하세요")
print_n_times("반갑습니다",3)
# 기본 매개변수는 만약에 밑에서 호출할 떄 매개변수를 입력하지않으면 들어갈 기본 셋팅같은 느낌이다.
# 밑에서 호출할 때 지정을 하면 기본매개변수 대신에 입력한 매개변수가 들어갑니다.