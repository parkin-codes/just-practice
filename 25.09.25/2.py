movie = {
    "title": "Inception",
    "year": 2010,
    "rating": {
        "imdb": 8.8,
        "rotten_tomatoes": "87%"
    },
    "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
}

for key in movie:
    if key == "rating":
        for i in movie[key]:
            print(i,':',movie[key][i])
    elif key == "actors":
        for j in movie[key]:
            print(key,':',j)
    else:
        print(key,':',movie[key])