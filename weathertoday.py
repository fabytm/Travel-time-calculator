from weather import Weather, Unit

def weather_today(city):
    weather = Weather(unit=Unit.CELSIUS)
    weather_location = weather.lookup_by_location(city)
    weather_data = weather_location.forecast

    return weather_data[0] #return all weather data for today