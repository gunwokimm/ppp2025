def average(nums):
    return sum(nums)/ len(nums)

def get_weather_data(fname,col_idx):
    weather_datas =[]
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def count_bigger_days(nums,criteria):
    basket = []
    for num in nums:
        if num >= criteria:
            basket.append(num)
            return len(basket)
        
def get_rain_events(rainfalls):
    events = []
    c_days = 0
    for rain in rainfalls:
        if rain > 0:
            c_days += 1 
        else:
            if c_days >0:
                events.append(c_days)
            c_days = 0
    if c_days > 0:
        events.append(c_days)
    

    return events

def largest_rainfall(rainfalls):
    largest_rainfall = rainfalls[0]
    for rainfall in rainfalls:
        if largest_rainfall < rainfall:
            largest_rainfall = rainfall
    
    return largest_rainfall

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


def main():
    filename = "hw10/weather(146)_2022-2022.csv"
    # 1번
    tavg = get_weather_data(filename, 4)
    print(f"일평균 기온은{average(tavg):.2f}")
    
    #2번
    rainfalls =  get_weather_data(filename,9)
    count_over5_rain = count_bigger_days(rainfalls, 5)
    count_over5_rain = len([x for x in rainfalls if x >=5])
    print(f"5mm이상 강우일수 = {count_over5_rain}")
    
    #3번
    print(f"총 강수량은 = {sum(rainfalls):,.1f}mm")
    
    #4번
    print(f"최장연속강수일수 = {max(get_rain_events(rainfalls))}일")

    #5번
    print(f"최대 강수량은{largest_rainfall(rainfalls)}입니다.")

    #6번
    top3_tmax = sorted(get_weather_data(filename,3))[-3:][::-1]
    print(f"가장 높았던 최고기온 3개는{top3_tmax}입니다.")

    #7번
    months= get_weather_data_int(filename, 1)
    print(f"여름철 강수량은{sumifs(rainfalls,months,selected=[6,7,8]):.1f}입니다.")

    #8번
    filename_20yr = "hw10/weather(146)_2001-2022.csv"
    years = get_weather_data_int(filename_20yr, 0)
    rainfalls = get_weather_data(filename_20yr, 9)
    print(f"2021년 총 강수량은{sumifs(rainfalls,years,selected=[2021]):.1f}입니다")
    print(f"2022년 총 강수량은{sumifs(rainfalls,years,selected=[2022]):.1f}입니다")

if __name__ =="__main__":
    main()
