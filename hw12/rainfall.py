def average(nums):
    return sum(nums) / len(nums)

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

def largest_rainfall(rainfalls):
    largest_rainfall = rainfalls[0]
    for rainfall in rainfalls:
        if largest_rainfall < rainfall:
            largest_rainfall = rainfall
    
    return largest_rainfall

def main():
    filename = "hw12/weather(146)_2020-2020.csv"

    tavg = get_weather_data(filename,4)
    print(f"일평균 기온은{average(tavg):.2f}")

    #5mm이상
    rainfalls = get_weather_data(filename,9)
    count_over5_rain = count_bigger_days(rainfalls, 5)
    count_over5_rain = len([x for x in rainfalls if x >=5])
    print(f"5mm이상 강우일수 = {count_over5_rain}")

    #총강수량
    print(f"총 강수량은 = {sum(rainfalls):,.1f}mm")

if __name__ =="__main__":
    main()