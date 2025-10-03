money = 10000
print("1. 입금 | 2. 출금 | 3. 잔액확인 | 4. 종료")
while True:
    menu = input("메뉴 선택: ")
    if menu == "1" :
        in_money = input("입금할 금액: ")
        print(f"{in_money}원이 입금되었습니다.")
        money += int(in_money)
        print(f"현재 잔액: {money}")
    elif menu == "2" :
        out_money = input("출금할 금액: ")
        print(f"{out_money}원이 출금되었습니다.")
        money -= int(out_money)
        print(f"현재 잔액: {money}")
    elif menu == "3" :
        print(f"현재 잔액: {money}")
    elif menu == "4" :
        print("ATM을 종료합니다.")
        break
    else :
        print('잘못된 접근입니다.')
