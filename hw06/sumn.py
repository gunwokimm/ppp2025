def sum_n(n):
    return (n*(n+1))/2

def main():
    n = int(input("n을 입력해주세요 =>"))
    sum = sum_n(n)
    print(f"{n}까지의 합은{sum}입니다.")

if __name__ =="__main__":
    main()