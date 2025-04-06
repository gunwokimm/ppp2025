def get_range_list(n):
    nums = []
    for i in range(n):
        nums.append(i+1)
    return nums


    
def main():
    # n = int(input("입력하시오"))
    n = 10
    print(f"{get_range_list(n)}")


if __name__ =="__main__":
    main()