charactor = {
    'name':'히어로',
    'level':'273',
    'items':{
        'weapon':'제네시스 투핸드소드',
        'armor_set':'아케인셰이드',
    },
    'skill':['레이징 블로우','인레이지','돌진']
}

#for 반복문을 사용합니다.
print('# 조건문 사용')
for key in charactor:
    if key == 'items':
        for i in charactor[key]:
            print(i,':',charactor[key][i])
    elif key == 'skill':
        for j in charactor[key]:
            print(key,':',j)
    else:
        print(key,':',charactor[key])
