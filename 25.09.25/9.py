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
    if isinstance(movie[key], str):
        print(f'{key} : {movie[key]}')
    elif isinstance(movie[key], dict):
        for i in movie[key]:
            print(f'{i} : {movie[key][i]}')
    elif key == "actors":
        print('출연 배우:')
        for j in movie[key]:
            print(j)
    elif key == "awards":
        print('수상 경력:')
        for k in movie[key]:
            print(f'{k["year"]} - {k["name"]}({k["category"]})')