movie = {
    "title": "Interstellar",
    "year": 2014,
    "director": "Christopher Nolan",
    "rating": {
        "imdb": 8.6,
        "rotten_tomatoes": "72%",
        "metacritic": 74
    },
    "actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
    "awards": [
        {"year": 2015, "name": "Academy Award", "category": "Best Visual Effects"},
        {"year": 2015, "name": "BAFTA Award", "category": "Best Special Visual Effects"},
        {"year": 2015, "name": "Saturn Award", "category": "Best Science Fiction Film"}
    ]
}

for key in movie:
    if type(movie[key]) is str:
        print(f'{key} : {movie[key]}')
    elif type(movie[key]) is dict:
        print('평점:')
        for i in movie[key]:
            print(f'{i} : {movie[key][i]}')
    elif movie[key] == "actors":
        print('출연 배우:')
        for k in movie[key]:
            print(movie[key][k])
    elif movie[key] == "awards":
        print(f'{k["year"]} - {k["name"]}({k["category"]})')