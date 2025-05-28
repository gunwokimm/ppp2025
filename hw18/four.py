import requests
import pandas as pd


def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def get_total_jeonrainfall():
    filename = "weather(146)_rainfall_2019.csv"
    download_weather(146, 2019,filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    jeonrainfall = (df["rainfall"].sum())
    # print(f"{jeonrainfall:.1f}")
    return jeonrainfall

def get_total_suwonrainfall():
    filename = "weather(119)_rainfall_2019.csv"
    download_weather(119, 2019, filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    suwonrainfall = (df["rainfall"].sum())
    # print(f"{suwonrainfall:.1f}")
    return suwonrainfall

def dif_total_rainfall():
    jeon_total = get_total_jeonrainfall()
    suwon_total = get_total_suwonrainfall()
    dif = abs(jeon_total - suwon_total)
    return(f"{dif:.1f}")

# print(dif_total_rainfall())
   

