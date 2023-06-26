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

plt.style.use('ggplot')
# print(df.info())

# df.fillna(method='ffill', inplace=True) # method=bfill
df = df.fillna(method='ffill')
# print(df.head())

# mask 연산 -> df[df[(조건)]]
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
print('>>> mask.head(25)')
print(mask.head(25))
df_seoul = df[mask]
print('df_seoul의 길이 : ', len(df_seoul)) # 17
print('>>> df_seoul.head(10)')
print(df_seoul.head(10))
# df.iloc[19:,:]
# df.drop(.., axis=0)

df_seoul = df_seoul.drop(['전출지별'], axis=1) # axis=1 -> 칼럼 자체를 지움
df_seoul.set_index('전입지별', inplace=True)
# print(df_seoul.head())

# 서울->경기 유입
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
plt.plot(sr_one, markersize=5, marker='*', color='olive')

plt.show()







# df = pd.read_excel("남북한발전전력량.xlsx")





