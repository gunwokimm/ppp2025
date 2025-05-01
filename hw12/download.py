import os
import requests

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="utf-8-sig")as f:
        resp = requests.get(URL)
        resp.encoding = "utf-8"
        f.write(resp.text)

def main():
    filename = "hw13/weather(146)_2020-2020.csv"
    if not os.path.exists(filename):
        download_weather(146, 2020, filename)

if __name__ =="__main__":
    main()