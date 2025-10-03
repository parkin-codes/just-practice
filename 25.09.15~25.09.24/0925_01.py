a ={
    '이름':'박병인',
    '나이':'27세',
    '주소':['성북구','석관동','전주집'],
    '고향':'부산'
}

print(a['이름'])
print(a['나이'])
print(a['주소'])
print(a['고향'])

a['성별']='남'
print('-'*20)
print()
print(a['성별'])
del a['나이']
print()
print(a)