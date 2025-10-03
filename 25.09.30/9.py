output = [ a for a in range(1,100 + 1) if f'{a:b}'.count('0') == 1]
for i in output:
    print(f"{i} : {i:b}")
print('합계 :',sum(output))