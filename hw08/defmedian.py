def text2list(text):
    text_list = text.split()
    nums = []
    for num_text in text_list:
        nums.append(int(num_text))
    return nums
    
def total(nums):
    return len(nums)

def max_num(nums):
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num 
    return max_num

def min_num(nums):
    min_num = nums[0]
    for num in nums:
        if min_num > num:
            min_num = num
    return min_num
    


def average(nums):
    return sum(nums)/len(nums)

def median(nums):
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list)//2]


def main():
    input_text = "5 10 3 4 7"
    nums = text2list(input_text)

    print(f"총 숫자의 개수는{len(nums)}입니다!")
    print(f"주어진 리스트는{nums}입니다.")
    print(f"평균값은 {average(nums):.1f}입니다.")
    print(f"최대값은{max_num(nums)}입니다.")
    print(f"최솟값은{min_num(nums)}입니다.")
    print(f"중앙값은{median(nums)}입니다.")
    

if __name__ =="__main__":
    main()