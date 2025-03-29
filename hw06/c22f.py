def c2f(t_c):
    return (t_c * 9/5) + 32

def main():
    temp_c = int(input("값을 입력하시오 =>"))
    temp_f = c2f(temp_c)
    
    print(f"{temp_c}C =>{temp_f:.1f}F 입니다.")

if __name__ == "__main__":
    main()