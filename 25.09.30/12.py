dna = input('염기 서열을 입력해주세요 :')
dict_dna = {}

for i in dna:
    if i == 'a' :
        dict_dna["a"]=dna.count("a")
    elif i == 'c':
        dict_dna["c"]=dna.count("c")
    elif i == "t":
        dict_dna["t"]=dna.count("t")
    elif i == "g":
        dict_dna["g"]=dna.count("g")

for i,v in dict_dna.items():
    print(f"{i}의 갯수 : {v}개")