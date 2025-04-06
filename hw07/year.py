def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            return False
    else:
        return False   

def main():
    year = int(input("연을 입력하시오=>"))
    print(f"{is_leap_year(year)}!")
    if is_leap_year(year):
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")
   
if __name__ == "__main__":
   main()
