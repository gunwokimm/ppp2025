eat_orange =int(input("오렌지 g 입력하세요."))
eat_strawberry = int(input("딸기 g 입력하세요."))
eat_banana = int(input("바나나 g 입력하세요."))


calories = {"한라봉":50/100,"딸기":34/100,"바나나":77/100}
total_calories = calories["한라봉"]* eat_orange + calories["딸기"]*eat_strawberry + calories["바나나"] * eat_banana
print(total_calories)