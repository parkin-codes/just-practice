player = {
    "id": "user001",
    "level": 15,
    "inventory": {
        "potion": 5,
        "gold": 320,
        "sword": "iron blade"
    },
    "quests": ["튜토리얼 클리어", "슬라임 10마리 처치", "첫 보스 클리어"]
}

for key in player:
    if type(player[key]) is dict:
        for i in player[key]:
            print(f"{i} : {player[key][i]}")
    elif type(player[key]) is list:
        for k in player[key]:
            print(f"{key} : {k}")
    else:
        print(f"{key} : {player[key]}")