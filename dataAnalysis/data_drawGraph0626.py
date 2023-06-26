import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

# 모든 칼럼 확인가능
pd.set_option('display.max_columns', None)

"""
# header = None 으로 지정할 필요 있음. 데이터 첫줄에 칼럼이 없어서
df = pd.read_csv("../Data/auto-mpg.csv", header=None)

# 열이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower",
              "weight", "acceleration", "model year", "origin", "name"]

# mpg 칼럼을 히스토그램으로 표현
df_mpg = df['mpg'] # df.mpg
df_mpg.plot.hist(bins=8)
plt.show()

# 산점도 형태로 그래프 그리기
df.plot.scatter(x='weight', y='mpg')
# df.plot(kind='scatter', x='weight', y='mpg') # 이렇게 작성할수도 있음
plt.show()

df_cy_mpg = df[['cylinders', 'mpg']] # df.mpg
df_cy_mpg.plot.box()
plt.show()
"""

df = pd.read_excel('../Data/시도별 전출입 인구수.xlsx')
# print(df.head())

# header=None 있으면 경기도가 아닌 타 지역으로의 이동(ex.서울 => 대구)의 경우 리스트 변환이 필요함
# x = seoul_daegu.index.tolist()  # 인덱스를 리스트로 변환
# y = seoul_daegu.tolist()  # 값들을 리스트로 변환

plt.style.use('ggplot')
# print(df.info())

# df.fillna(method='ffill', inplace=True) # method=bfill
df = df.fillna(method='ffill')
# print(df.head())

# mask 연산 -> df[df[(조건)]]
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
# print('>>> mask.head(25)')
# print(mask.head(25))
df_seoul = df[mask]
# print('df_seoul의 길이 : ', len(df_seoul)) # 17
# print('>>> df_seoul.head(10)')
# print(df_seoul.head(10))
# df.iloc[19:,:]
# df.drop(.., axis=0)

df_seoul = df_seoul.drop(['전출지별'], axis=1) # axis=1 -> 칼럼 자체를 지움
df_seoul.set_index('전입지별', inplace=True)
# print(df_seoul.head())

# 서울 ==> 경기 유입
sr_one = df_seoul.loc['경기도']
# print(sr_one)

# 사이즈 : 튜플 형태. inch(가로, 세로). 1인치 = 2.5cm
plt.figure(figsize=(10, 6))

plt.title("서울==>경기 이동 인구수")
plt.xlabel("기간")
plt.xticks(rotation=90)
plt.ylabel("이동 인구수")

# 범례지정 legend
plt.legend(labels="서울==>경기", loc="best")

# plt.plot(sr_one)
plt.plot(sr_one, markersize=5, marker='*', color='black')

plt.show()

"""
왜지???????? 다 똑같은데 왜 대구만 안뜨지??????????????????????????????????????????????????????????????????????????????????????????????


# 서울 ==> 대구 인원 가지고 오기
# seoul_daegu = (df['전출지별'] == '서울특별시') & (df['전입지별'] == '대구광역시')
seoul_daegu = df_seoul.loc['대구광역시']

# 사이즈 : 튜플 형태. inch(가로, 세로). 1인치 = 2.5cm
plt.figure(figsize=(10, 6))

plt.title("서울==>대구 이동 인구수")
plt.xlabel("기간")
plt.xticks(rotation=90)
plt.ylabel("이동 인구수")

# 범례지정 legend
plt.legend(labels="서울==>대구", loc="best")

plt.plot(seoul_daegu, markersize=5, marker='*', color='blue')

plt.show()

"""

# 서울 ==> 충남 이동 인구수
seoul_chungnam = df_seoul.loc['충청남도']

# 사이즈 : 튜플 형태. inch(가로, 세로). 1인치 = 2.5cm
plt.figure(figsize=(10, 6))

plt.title("서울==>충남 이동 인구수")
plt.xlabel("기간")
plt.xticks(rotation=90)
plt.ylabel("이동 인구수")

# 범례지정 legend
plt.legend(labels="서울==>충남", loc="best")

plt.plot(seoul_chungnam, markersize=5, marker='*', color='red')

plt.show()

# 서울 ==> 경북 이동 인구수
seoul_gyeongbuk = df_seoul.loc['경상북도']

# 사이즈 : 튜플 형태. inch(가로, 세로). 1인치 = 2.5cm
plt.figure(figsize=(10, 6))

plt.title("서울==>경북 이동 인구수")
plt.xlabel("기간")
plt.xticks(rotation=90)
plt.ylabel("이동 인구수")

# 범례지정 legend
plt.legend(labels="서울==>경북", loc="best")

plt.plot(seoul_gyeongbuk, markersize=5, marker='*', color='red')

plt.show()

# 서울 ==> 강원도 이동 인구수
seoul_gangwon = df_seoul.loc['강원도']

# 사이즈 : 튜플 형태. inch(가로, 세로). 1인치 = 2.5cm
plt.figure(figsize=(10, 6))

plt.title("서울==>강원 이동 인구수")
plt.xlabel("기간")
plt.xticks(rotation=90)
plt.ylabel("이동 인구수")

# 범례지정 legend
plt.legend(labels="서울==>강원", loc="best")

plt.plot(seoul_gangwon, markersize=5, marker='*', color='red')

plt.show()