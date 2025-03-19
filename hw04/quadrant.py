X = int(input("x의 좌표를 입력하시오."))
Y = int(input("y의 좌표를 입력하시오."))

if X>0 and Y>0:
    print("1사분면입니다.")
elif X<0 and Y>0:
    print("2사분면입니다.")
elif X<0 and Y<0:
    print("3사분면입니다.")
else:
    print("4사분면입니다.")