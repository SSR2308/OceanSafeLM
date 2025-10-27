def get_weather_data(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"5fd993659ef1c5695e180f1687ead4f4"}&units=imperial"
    res = requests.get(url)
    data = res.json()
    return {
        "Temperature (°F)": round(data["main"]["temp"], 2),
        "Weather": data["weather"][0]["description"].title(),
        "UV Index": "Check local UV forecast"
    }

