
from geopy.geocoders import Nominatim


def get_weather(city: str) -> str:
    loc = Nominatim(user_agent="GetLoc")
    try:
        getLoc = loc.geocode(city)
    except:
        raise Exception("City not found")
        
    latitude = getLoc.latitude
    longitude = getLoc.longitude
    api_key = 1
    request_url=f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,daily,alerts&appid={api_key}"
