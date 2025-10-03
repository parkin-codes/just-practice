weather_data = {
    "city": "Seoul",
    "temperature": {
        "morning": 18,
        "afternoon": 25,
        "evening": 21
    },
    "forecast": [
        {"day": "Mon", "condition": "Sunny", "high": 26, "low": 17},
        {"day": "Tue", "condition": "Cloudy", "high": 23, "low": 16},
        {"day": "Wed", "condition": "Rainy", "high": 20, "low": 15}
    ],
    "alerts": ["폭염 주의보", "강풍 주의보"]
}

for key in weather_data:
    if key == "temperature":
        for i in weather_data[key]:
            print(i,':',weather_data[key][i])
    elif key == "forecast":
        for j in weather_data[key]:
            for l in j:
                print(l,':',j[l])
    elif key == "alerts":
        for k in weather_data[key]:
            print(key,':',k)
    else:
        print(key,':',weather_data[key])