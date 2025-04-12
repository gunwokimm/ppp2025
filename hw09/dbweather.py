def read_tavg(filename):
    result = []
    with open(filename,encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            tavg = float(tokens[4])
            result.append(tavg)
    return result
        
           

def read_rainfall(filename):
    result = []
    with open(filename,encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            rainfall = float(tokens[-3])
            if rainfall > 5:
                result.append(rainfall)
    return result            





def main():
    averge_weather = read_tavg("hw09/weather(146)_2022-2022.csv")
    total_rainfall = read_rainfall("hw09/weather(146)_2022-2022.csv")
    print(f"연평균기온은{sum(averge_weather)/len(averge_weather):.1f}도입니다")
    print(f"5mm이상인 강우일수는 {len(total_rainfall)}입니다.")
    print(f"총 강우랑은{sum(total_rainfall)}입니다.")    


if __name__ =="__main__":
    main()