n = int(input("별의 개수를 작성하시오 =>"))

for i in range(n):
    print('*'*(i+1),' '*2*(n-(i+1)),'*'*(i+1)) 
