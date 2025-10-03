user_scores = input("점수를 쉼표단위로 입력해주세요")
number = [int(i.strip()) for i in user_scores.split(",")]

print(sum(number))