fruit_eat = {"한라봉":150,"딸기":200,"바나나":250}
fruit_cal ={"한라봉":50/100,"딸기":34/100,"바나나":77/100}
eat_list = ["한라봉","딸기","딸기","바나나"]

total = 0
for eat in eat_list:

    total += fruit_eat[eat]*fruit_cal[eat]
print(f"총 섭취량은{total}kcal입니다!")