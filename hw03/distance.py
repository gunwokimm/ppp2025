X1 = int(input("x축의 거리를 입력하시오"))
X2 = int(input("두번쨰 x축의  거리를 입력하시오"))
Y1 = int(input("y축의 거리를 입력하시오"))
Y2 = int(input("두번쨰 y축의 거리를 입력하시오"))

import math
distance = math.sqrt((X1-X2)**2 + (Y1-Y2)**2)
print("두 지점 사이의 거리는 {}입니다.".format(distance))