import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


# === 1. 포지션별 데이터 === #
positions_data = {
    "1B": pd.DataFrame({
        "선수명": ["오스틴", "디아즈", "양석환", "채은성", "나승엽", "고명준", "최주환"],
        "팀": ["엘지", "삼성", "두산", "한화", "롯데", "ssg", "키움"],
        "WAR": [2.61, 1.7, 1.01, 0.77, 0.59, 0.46, 0.25],
        "OPS": [1.011, 0.984, 0.748, 0.835, 0.773, 0.742, 0.753],
        "HR": [17, 22, 6, 9, 7, 7, 4],
        "RBI": [47, 64, 23, 31, 31, 30, 31],
    }),
    "2B": pd.DataFrame({
        "선수명": ["박민우","고승민","류지혁","정준재"],
        "팀": ["엔씨", "롯데", "삼성" ,"ssg"],
        "WAR": [2.24, 1.28, 0.66, 0.03],
        "OPS": [0.807, 0.751, 0.695, 0.556],
        "HR": [0, 2, 0, 0],
        "RBI": [22, 20, 20,12],
    }),
    "3B": pd.DataFrame({
        "선수명": ["문보경","송성문","황재균","강승호","김영웅","노시환","김휘집"],
        "팀": ["엘지", "키움", "kt" ,"두산","삼성","한화","엔씨"],
        "WAR": [3.50, 3.03, 1.30, 1.00, 0.79, 0.75, -1.06],
        "OPS": [0.994,0.828,0.772,0.623,0.756,0.731,0.576],
        "HR": [12,10,2,3,8,11,5],
        "RBI": [44,36,20,21,28,40,14],
    }),
    "OF": pd.DataFrame({
        "선수명": ["김성윤","레이예스","플로리얼","김현수","윤동희","로하스","권희동","박해민","케이브","정수빈"],
        "팀": ["삼성","롯데","한화","엘지","롯데","kt","엔씨","엘지","두산","두산"],
        "WAR": [3.03, 2.33, 1.78, 1.62, 1.56, 1.53, 1.47, 1.41, 1.38, 1.29],
        "OPS": [0.929, 0.895, 0.784, 0.798, 0.802, 0.792, 0.793, 0.635, 0.730, 0.692],
        "HR": [2, 8, 8, 5, 4, 8, 3, 0, 4, 3 ],
        "RBI": [26,50,26,40,29,26,16,12,26,17],
    }),}

selected_position = input("어떤 포지션의 골든글러브가 궁금하세요? (예: 1B, 2B,OF): ").upper()

if selected_position in positions_data:
    df = positions_data[selected_position].copy()
    df['GoldenGloveScore'] = df['WAR']*3 + df['OPS']*2 + df['HR']*0.5 + df['RBI']*0.3
    df_sorted = df.sort_values(by='GoldenGloveScore', ascending=False).reset_index(drop=True)
    df_sorted.index += df_sorted.index + 1

    plt.figure(figsize=(10,6))
    plt.bar(df_sorted['선수명'], df_sorted['GoldenGloveScore'], color='green')
    plt.title(f'KBO {selected_position} 골든글러브 예측 점수')
    plt.xlabel('선수명')
    plt.ylabel('골든글러브 점수')
    plt.grid(axis='y')
    plt.show()

    # 상위 3명 출력
    top3 = df_sorted[['선수명','GoldenGloveScore']].head(3).copy()
    top3.insert(0,'순위', range(1,4))
    print(f"{selected_position} 골든글러브 예상 상위 3명")
    print(top3)

