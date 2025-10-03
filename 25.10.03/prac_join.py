a =["홍길동", "김안녕", "밤양갱"]
index_a = enumerate(a)
with open("name_tag.txt","w") as file:
    file.write("\n".join([f"{i+1}.{name}" for i, name in index_a]))

numbers = [1, 2, 3, 4, 5]

result = " + ".join(str(i) for i in numbers)
print(f"{result} = {sum(numbers)}")