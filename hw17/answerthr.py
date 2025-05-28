def get_weather_data(fname,col_idx):
    weather_datas = []
    with open(fname, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def maximum_temp_gap(tmax, tmin):
    max_gap = tmax[0] - tmin[0]
    for i in range(len(tmax)):
        tx = tmax[i]
        tm = tmin[i]
        gap = tx - tm
        if max_gap < gap:
            max_gap = gap
        
    return max_gap


def get_max_gap():
    filename = "hw16/weather(146)_2024-2024.csv"
    t_max = get_weather_data(filename, 4)
    t_min = get_weather_data(filename, 3)
    max_gap = maximum_temp_gap(t_max,t_min)
    return max_gap

print(get_max_gap())
