def get_weather_data(fname,col_idx):
    weather_dates =[]
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append(float(tokens[col_idx]))

    return weather_dates

def get_total_jeonrainfall():
    filename = "hw16/weather(146)_rainfall_2024-2024.csv"
    rainfalls = get_weather_data(filename, 3)
    return sum(rainfalls)

def get_total_suwonrainfall():
    filename = "hw16/weather(119)_rainfall_2024-2024.csv"
    rainfalls = get_weather_data(filename,3)
    return sum(rainfalls)

def get_rainfall_difference():
    jeon_total = get_total_jeonrainfall()
    suwon_total = get_total_suwonrainfall()
    dif = abs(jeon_total - suwon_total)
    return round(dif,1)

print(get_rainfall_difference())