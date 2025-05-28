def get_weather_data(fname,col_idx,target_year):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            try:
                year = int(tokens[0])
                if year == target_year:
                    weather_datas.append(float(tokens[col_idx]))
            except (ValueError, IndexError):
                continue
        return weather_datas
                

    return weather_datas



def get_top_weather():
    filename_20yr = "hw16/weather(146)_2001-2022.csv"
    target_year = 2022
    top_tmax = max(get_weather_data(filename_20yr,4, target_year))
    return top_tmax

print(get_top_weather())