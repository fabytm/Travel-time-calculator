from forecastiopy import *

def weather_today(lat, long, API_file):
    with open(API_file) as Weather_API_file:
        Weather_API_key = Weather_API_file.read().rstrip("\n")

    weatherObject = ForecastIO.ForecastIO(Weather_API_key,
                                units=ForecastIO.ForecastIO.UNITS_SI,
                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                latitude=lat, longitude=long)
    if weatherObject.has_daily():
        daily = FIODaily.FIODaily(weatherObject)
        todays_weather = daily.get_day(0)
        summary = todays_weather["summary"]
        high = round(todays_weather["temperatureHigh"])
        low = round(todays_weather["temperatureLow"])
        precip_prob = round(todays_weather["precipProbability"] * 100)
    else:
        print('No Daily data')
    return summary,high,low,precip_prob

