orders = [
    {"customer": "민수", "items": [
        {"name": "노트북", "price": 1200000, "quantity": 1},
        {"name": "마우스", "price": 25000, "quantity": 2}
    ]},
    {"customer": "영희", "items": [
        {"name": "키보드", "price": 55000, "quantity": 1},
        {"name": "모니터", "price": 300000, "quantity": 2}
    ]},
    {"customer": "철수", "items": [
        {"name": "USB", "price": 15000, "quantity": 3}
    ]}
]
for ele in orders:
    print(f'[{ele["customer"]}님의 주문 내역]')
    total = 0
    for i in ele["items"]:
        item_total = i["price"]*i["quantity"]
        total += item_total
        print(f'{i["name"]} {i["quantity"]} : {item_total}원')
        print(f'총 합계: {total}원')