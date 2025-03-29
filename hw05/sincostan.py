import math

for i in range(1, 10+1):
    c = i * 15
    sinx = math.sin(math.pi * (c/180))
    cosx = math.cos(math.pi * (c/180))
    tanx = math.tan(math.pi * (c/180))
    radian = math.pi*(i/180)
    
    print(f"sin|{sinx:.4f}| cos|{cosx:.4f}| tan|{tanx:.4f}| radian|{radian:.4f}")    