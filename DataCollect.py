import pandas as pd
import requests


# Define a function to read the location csv file
# And check the location is in our database or not
def check_loc(postcode, suburb):
    # Read the location csv file
    df = pd.read_csv("location.csv")
    result = df[(df["postcode"] == int(postcode)) & (df["suburb"] == suburb)]
    return result


def get_weather_cur(postcode, suburb):
    # Get the latitude and longitude based on the postcode and suburb information in the database table
    loc_result = check_loc(postcode, suburb)
    lat = loc_result["latitude"].values[0]
    lon = loc_result["longitude"].values[0]
    key = "d32542473437f300dfdec104552b7f65"
    main_url = "https://api.openweathermap.org/data/3.0/onecall?"
    req_url = main_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + key
    # Get the UV level
    response = requests.get(req_url)
    return response.json()


def get_uv_level(weather_info):
    # Get main weather information
    uv_level = weather_info['current']['uvi']
    return uv_level


if __name__ == "__main__":
    uv = get_weather_cur(3000, "Melbourne")
    print(get_uv_level(uv))
