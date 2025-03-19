mandarin = int(input("섭취량을 g으로 입력하세요"))
strawberry = int(input("섭취량을 g입력하세요"))
banana = int(input("섭취량을 g입력하세요"))

mandarin_kcal = mandarin*50/100
strawberry_kcal = strawberry*34/100
banana_kcal = banana*77/100

print("한라봉의 ㎉는{}이고, 딸기의 ㎉는 {}이고, 바나나의 ㎉는{}입니다.".format(mandarin_kcal,strawberry_kcal,banana_kcal))