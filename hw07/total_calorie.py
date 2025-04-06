def total_calorie(fruits,fruits_calorie_dic):
    # total_calorie = fruits["딸기"]*fruits_calorie_dic["딸기"]
    # total_calories = fruits["한라봉"]*fruits_calorie_dic["한라봉"]
    # total = total_calorie + total_calories
    # return total
    total_calorie = 0
    for fruit in fruits:
        total_calorie += fruits[fruit]*fruits_calorie_dic[fruit]
    return total_calorie

    
def main():
    fruits ={"딸기":300, "한라봉":150} 
    fruits_calorie_dic={"한라봉":50/100,"딸기":34/100,"바나나":77/100}
    print(f"먹은 양은{total_calorie(fruits,fruits_calorie_dic)}입니다.")

if __name__ =="__main__":
    main()