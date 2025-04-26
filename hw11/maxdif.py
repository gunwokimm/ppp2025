def get_weather_data(fname,col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def maximum_temp_gap(dates, tmax, tmin):
    max_gap = tmax[0] - tmin[0]

    for i in range(len(dates)):
        date = dates[i]
        tx = tmax[i]
        tm = tmin[i]
        gap = tx - tm
        if max_gap < gap:
            max_gap = gap
            max_gap_date = date
    return [max_gap_date, max_gap]

def get_weather_date(filename):

    weather_dates = []
    with open(filename,encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])

    return weather_dates

def main():
    filename = "hw11/weather(146)_2001-2022.csv"
    dates = [[2021,1,1],[2021,1,2],[2021,1,3]]
    dates = get_weather_date(filename)
    t_max = get_weather_data(filename, 5)
    t_min = get_weather_data(filename, 7)
    max_gap_date, max_gap = maximum_temp_gap(dates, t_max,t_min)
    print(f"일교차가 가장 큰 일자는{max_gap_date}이고,"f"해당일의 일교차는{max_gap}도 입니다.")

if __name__ =="__main__":
    main()        
