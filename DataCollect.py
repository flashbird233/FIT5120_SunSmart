import pandas as pd
import requests


# Define a function to read the location csv file
# And check the location is in our database or not
def check_loc(postcode):
    # Read the location csv file
    df = pd.read_csv("location.csv")
    # Check the location is in our database or not
    result = df[df["postcode"] == int(postcode)]
    return result


def get_suburb(postcode):
    df = check_loc(postcode)
    if len(df) == 0:
        return "No location found for the given postcode."
    else:
        return df["suburb"].values[0]


def get_weather_cur(postcode):
    # Get the latitude and longitude based on the postcode and suburb information in the database table
    loc_result = check_loc(postcode)
    lat = loc_result["latitude"].values[0]
    lon = loc_result["longitude"].values[0]
    print(lat, lon)
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
        sug = "No protection needed. You can safely stay outside using minimal sun protection."
        cloth_sug = None
        suns_sug = None
        return sug, cloth_sug, suns_sug
    elif uv_level <= 7:
        sug = "Protection needed. Seek shade during late morning through mid-afternoon."
        cloth_sug = "Wear protective clothing, a wide-brimmed hat, and sunglasses."
        suns_sug = "When outside, Generously apply broad-spectrum SPF-15 or higher sunscreen on exposed skin."
        return sug, cloth_sug, suns_sug
    else:
        sug = "Extra protection needed. Be careful outside, especially during late morning through mid-afternoon."
        cloth_sug = "Wear protective clothing, a wide-brimmed hat, and sunglasses."
        suns_sug = "Generously apply a minimum of SPF-15, broad-spectrum sunscreen on exposed skin."
        return sug, cloth_sug, suns_sug


if __name__ == "__main__":
    wea = get_weather_cur(810)
    print(wea)
    print(get_uv_level(wea))

