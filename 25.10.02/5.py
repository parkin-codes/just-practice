def call_10_times(콜백함수):
    for i in range(10):
        콜백함수(i)

def print_hello(매개변수):
    print("안녕하세요",매개변수)
    
call_10_times(print_hello)