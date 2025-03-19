weight = int(input("몸무게는 얼마인가요? =>"))
height = int(input("키가 얼마인가요? =>"))

height_m = height / 100
BMI = (weight / height_m**2)
print(BMI)