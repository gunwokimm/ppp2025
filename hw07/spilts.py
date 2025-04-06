from averge import averge
def main():
    # n = input("입력")
    n = "1,4,9,11"
    nums = []
    for i in n.split(","):
        nums.append(int(i))
    print(averge(nums))


if __name__ == "__main__":
    main()