output = ""
for i in range(1,20):
    for i in range(19,i,-1):
        output +=" "
    for k in range(i,2*i-1):
        output +="*"
    output += "\n"
print(output)