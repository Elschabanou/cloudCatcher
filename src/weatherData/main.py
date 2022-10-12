import requests
from geopy.geocoders import Nominatim


def get_weather(city: str) -> str:
    loc = Nominatim(user_agent="GetLoc")
    try:
        getLoc = loc.geocode(city)
    except:
        raise Exception("City not found")
    # test
    latitude = getLoc.latitude
    latitude = 33.44
    longitude = getLoc.longitude
    longitude = -94.04
    api_key = "65e18d8ec814590c386dffb416021cc6S"
    request_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly&appid={api_key}"
    response = requests.get(request_url)

    response = {
        "weather": {"main":"sunny"},
        "temp": "10.0",
        "rain" :"40", 
    }
    #print(response)
    kind_of_weather = response["weather"]["main"]
    temperature = response["temp"]
    probability_of_rain = response["rain"]
    message = f"Hey ure weather in city will be {kind_of_weather}, with a temperature of {temperature} degree and a probability {probability_of_rain} of rain "
    print(message)
    return message


