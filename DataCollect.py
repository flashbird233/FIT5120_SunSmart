import pandas as pd
import requests


# Define a function to remove blank spaces and convert the string to lower case
def clean_str(str_in):
    str_in = str(str_in)
    str_in = str_in.replace(" ", "")
    return str_in.strip().lower()


# Define a function to read the location csv file
# And check the location is in our database or not
def check_loc(post_sub):
    # Read the location csv file
    df = pd.read_csv("location.csv")
    post_sub = clean_str(post_sub)
    # clean the suburb
    df["suburb"] = [clean_str(x) for x in df["suburb"]]
    # Check the location is in our database or not
    try:
        postcode = int(post_sub)
        return df[df["postcode"] == postcode]
    except ValueError:
        return df[df["suburb"] == post_sub]


def get_suburb(post_sub):
    df = check_loc(post_sub)
    if len(df) < 1:
        return False
    else:
        return df["suburb"].values[0]


def get_weather_cur(post_sub):
    # Get the latitude and longitude based on the postcode and suburb information in the database table
    loc_result = check_loc(post_sub)
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
    test = check_loc("mel")
    print(len(test))

