weight = int(input("몸무게는 얼마인가요? =>"))
height = int(input("키가 얼마인가요? =>"))

height_m = height / 100
BMI = (weight / height_m**2)
if 23 <= BMI <= 24.9:
    print("비만 전단계")
elif 25 <= BMI <= 29.9:
    print("1단계 비만")
elif 30 <=BMI <= 34.9:
    print("2단계 비만")
elif BMI > 35:
    print("3단계 비만")
else:
    print("저체중입니다.")

print(BMI)