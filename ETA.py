import json
import traveltime
import weathertoday
import pushnotification
import spreadsheet
import datetime

with open('config.json') as config:
    config_data = json.load(config)


origin_coord = config_data["starting_point_coordinates"][0],config_data["starting_point_coordinates"][1]         #your origin coordinates
destination_coord = config_data["destination_point_coordinates"][0],config_data["destination_point_coordinates"][1]    #your destination
city = config_data["city"]

gmaps_key = config_data["google_maps_API_key"]
gsheets_key = config_data["google_sheets_API_key"]
gsheets_ID = config_data["google_sheet_ID"]
pushbullet_key = config_data["pushbullet_API_key"]


travel_time = traveltime.get_travel_time(origin_coord,destination_coord,gmaps_key)

print(travel_time)

sheet = spreadsheet.get_sheet(gsheets_key,gsheets_ID)

sheet_data = sheet.get_all_values() #get the updated sheet data
nr_of_rows = len(sheet_data)

current_hour = datetime.datetime.now().time().hour
current_min = datetime.datetime.now().time().minute

current_col_index = current_hour * 2 + 5     #4 is the offset for the first columns dedicated to the date and weather

if(current_min >= 30):
    current_col_index += 1                                      #if time is within second half of the hour, add one to the column index

print(current_col_index)
print(nr_of_rows)

if(current_col_index == 5):
    date = datetime.datetime.now()  # current time
    formatted_date = date.strftime("%d.%m.%Y")
    day_of_week = date.strftime("%A")
    weather = weathertoday.weather_today(city)
    print(weather.date)
    new_row_data = formatted_date, day_of_week, weather.low + "/" + weather.high, weather.text, travel_time
    sheet.append_row(new_row_data)
else:
    sheet.update_cell(nr_of_rows,current_col_index,travel_time)

if(current_hour == 8 and current_min < 30):
    try:
        pushnotification.push_to_iOS("Yesterday's average travel time to cross " + city + " was: " + sheet_data[nr_of_rows-2][-1] + "minutes."," ",pushbullet_key)
    except:
        print("PushBullet notifications don't work. Try verifying the key!")