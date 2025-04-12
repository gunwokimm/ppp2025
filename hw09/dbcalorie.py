def read_db(filename):
    calorie_dic = dict() #{}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            calorie_dic[tokens[0]] = int(tokens[1]) / int(tokens[2])
            print(line)
    
    return calorie_dic                            #외우기
            
def main():
    fruit_cal = read_db("hw09/calorie_db.csv")
    fruit_eat = {"쑥": 100,"바나나":100}

    total = 0
    for item in fruit_eat:
        total += (fruit_cal[item]*fruit_eat[item])

    print(f"{total}")
    

    # return{"한라봉":50/100,"딸기":34/100,"바나나":77/100}  #딕셔너리를 어떻게 만드느냐를 배운다. 
if __name__ =="__main__":
    main()