def get_weather_data(fname,col_idx):
    weather_datas =[]
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def get_weather_data_int(fname,col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(int(tokens[col_idx]))
        
    return weather_datas

def sumifs(rainfalls, months, selected = [6, 7, 8]):
    total = 0 
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain
    
    return total

def get_2015_rainfall():
    filename_20yr = "hw16/weather(146)_2001-2022.csv"
    years = get_weather_data_int(filename_20yr, 0)
    rainfalls = get_weather_data(filename_20yr, 9)
    total_rainfall = sumifs(rainfalls, years, selected =[2015])
    return round(total_rainfall,2)

print(get_2015_rainfall())
