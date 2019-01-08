import googlemaps

def get_travel_time(origin_coord,destination_coord,API_key):
    gmaps_api_file = open(API_key, 'r')
    gmaps_api_key = gmaps_api_file.read()

    gmaps = googlemaps.Client(key=gmaps_api_key)

    gmaps_result = gmaps.distance_matrix(origins=str(origin_coord)[1:-1], departure_time="now",
                                         destinations=str(destination_coord)[1:-1], mode="driving")   #[1:-1] in order to eliminate opening and closing parentheses

    travel_time = gmaps_result["rows"][0]["elements"][0]["duration_in_traffic"]["value"]

    return round(travel_time / 60)

def get_city_coordinates(city,API_key):
    gmaps_api_file = open(API_key, 'r')
    gmaps_api_key = gmaps_api_file.read()

    gmaps = googlemaps.Client(key=gmaps_api_key)

    gmaps_result = gmaps.geocode(city)
    coord = gmaps_result[0]["geometry"]["location"]
    latitude = coord["lat"]
    longitude = coord["lng"]
    return latitude, longitude

get_city_coordinates("Timisoara","Gmaps_key.txt")