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


# According to the UV index, we could give the sunscreen SPF suggestion
# https://www.epa.gov/sunsafety/uv-index-scale-0
def get_spf_sug(uv_level):
    if uv_level < 2:
        return "No protection needed. You can safely stay outside using minimal sun protection."
    elif uv_level <= 7:
        return ("""
        Protection needed. Seek shade during late morning through mid-afternoon. 
        When outside, generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin, 
        and wear protective clothing, a wide-brimmed hat, and sunglasses.
        """)
    else:
        return ("""
        Extra protection needed. Be careful outside, especially during late morning through 
        mid-afternoon. If your shadow is shorter than you, seek shade and wear protective clothing, 
        a wide-brimmed hat, and sunglasses, and generously apply a minimum of  SPF-15, 
        broad-spectrum sunscreen on exposed skin.
        """)


if __name__ == "__main__":
    uv = get_weather_cur(3000, "Melbourne")
    print(get_uv_level(uv))
