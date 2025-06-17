import requests
from bs4 import BeautifulSoup
import pandas as pd

# 요청 헤더 설정
headers = {'User-Agent': 'Mozilla/5.0'}

# 대상 URL
url = "https://statiz.sporki.com/stats/?m=main&m2=pitching&m3=default&so=WAR&ob=DESC&year=2025&sy=&ey=&te=&po=&lt=10100&reg=R&pe=&ds=&de=&we=&hr=&ha=&ct=&st=&vp=&bo=&pt=&pp=&ii=&vc=&um=&oo=&rr=&sc=&bc=&ba=&li=&as=&ae=&pl=&gc=&lr=&pr=50&ph=&hs=&us=&na=&ls=&sf1=&sk1=&sv1=&sf2=&sk2=&sv2="
# HTTP 요청
response = requests.get(url, headers=headers)

# 요청 성공 여부 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    
    # 테이블 존재 여부 확인
    if table:
        tbody = table.find('tbody')
        rows = tbody.find_all('tr')
        
        data = []
        for row in rows:
            cols = row.find_all('td')
            col_data = [col.get_text(strip=True) for col in cols]
            data.append(col_data)
        
        # 최대 열 수 확인
        max_cols = max(len(row) for row in data)
        
        # 열 수에 맞게 columns 리스트 생성
        columns = [f"Column{i+1}" for i in range(max_cols)]
        
        # 데이터프레임 생성
        df = pd.DataFrame(data, columns=columns)
        
        # CSV 파일로 저장
        df.to_csv('kbo_picters_player_stats_2025.csv', index=False, encoding='utf-8-sig')
        print("CSV 파일이 성공적으로 저장되었습니다: kbo_player_stats_2025.csv")
    else:
        print("테이블을 찾을 수 없습니다. 웹사이트 구조가 변경되었을 수 있습니다.")
else:
    print(f"HTTP 요청 실패: 상태 코드 {response.status_code}")
