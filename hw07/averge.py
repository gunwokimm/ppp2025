def averge(nums):
    avg = sum(nums)/len(nums)
    return avg

def main():
    nums = [1, 3, 5, 7, 9]
    print(f"숫자 합들의 평균은{averge(nums)}입니다.")

if __name__ == "__main__":
    main()