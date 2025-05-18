import random

CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
                'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
                'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def to_chosung(text):
    return ''.join([CHOSUNG_LIST[to_chosung_ch(ch)]for ch in text])

def to_chosung_ch(ch):
    return (ord(ch) - ord('가')) // 588

# def to_chosung(text):
#     full_text = []
#     for ch in text:
#         full_text.append(to_chosung_ch(ch))
#     return (full_text)



def main():
    problems = ["바나나","딸기","토마토","복숭아"]

    solution = problems[random.randrange(len(problems))]
    is_correct = False

    for i in range(3): #게임 기회
        answer = input(f"{to_chosung(solution)}?")
        if answer == solution:
            print("정답입니다.")
            is_correct = True
            break
        else:
            print("오답입니다")
    if is_correct:
        print("잘하셨습니다.")
    else:
        print("게임오버. 다시해보세요")
    
if __name__ == "__main__":
    main()