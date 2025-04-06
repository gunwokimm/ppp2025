from averge import averge

def main():
    text_input = "1, 3, 5, 7, 9, 11"
    avgs = text_input.split(",")
    nums = []

    for avg in avgs:
        nums.append(int(avg))
    print(f"숫자합의 평균은{averge(nums)}입니다.")

if __name__ == "__main__":
    main()

