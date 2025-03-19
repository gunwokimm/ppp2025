radius = int(input("반지름을 입력하세요."))

import math 
pi = math.pi
circle_circumference = 2*pi*radius
circle_area = pi*radius**2
print(f"원의 둘레는{circle_circumference:.1f}")
print(f"원의 넓이는{circle_area:.2f}")