def print_n_times(횟수, *리스트):
    print(리스트)
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)
        
문자열목록 = ["안녕","하세요","저는","박병인","입니다"]
print_n_times(2,*문자열목록)
