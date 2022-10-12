from operator import imod


import weatherData
import pytest

def test_get_weather():
    result = weatherData.get_weather("Tübingen")
    assert result == "Hey ure weather in city will be sunny, with a temperature of 10.0 degree and a probability 40 of rain"