import requests
import pandas as pd

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def temp_diff():
    filename = "weather(146)_2020.csv"
    download_weather(146,2020,filename)

    df = pd.read_csv(filename, skipinitialspace = True)
    df["tdiff"] =df["tmax"]- df["tmin"]
    t_diff = (df["tdiff"].max())
    return(t_diff)

# print(temp_diff())