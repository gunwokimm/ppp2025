def get_weather_data(filename):
    weather_datas = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            weather_datas.append(float(tokens[4])) 

    return weather_datas

def get_weather_date(filename):
    
    weather_dates = []
    with open(filename,encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])
    
    return weather_dates


def gdd_season(tavg,dates):
    temp_cum = 0
    base_temp = 5
    for i in range(len(tavg)):
        t = tavg[i]
        if dates[i][1] in [5,6,7,8,9]:
            if t >= base_temp:
                temp_cum += (t-base_temp)
    return temp_cum 

def gdd_per_year(tavg,dates,years):
    yearly_gdd ={}

    base_temp = 5
    for year in years:
        temp_cum = 0
        for i in range(len(dates)):
            if dates[i][0] == year:
                t = tavg[i]
                if t >= base_temp:
                    temp_cum += (t - base_temp)
        yearly_gdd[year] = temp_cum

    return yearly_gdd


def main():
    filename = "hw11/weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tavg = get_weather_data(filename)
    years = sorted(list([date[0]for date in dates]))

    yearly_gdd = gdd_per_year(tavg, dates, years)
    for year in yearly_gdd:
        print(f"{year}년 GDD는{yearly_gdd[year]:.2f}도일 입니다.")

if __name__ =="__main__":
    main()
    
   
