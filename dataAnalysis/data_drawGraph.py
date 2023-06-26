import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

"""
# 남북한발전전력량

df = pd.read_excel("남북한발전전력량.xlsx")
# print(df.info())
# print(df.head(10))

df1 = df.iloc[[0, 5], 2:]
print(df1)
# df1.plot.bar() # index : x축, 값 : y축, 칼럼 : 범례
# plt.show()

# transpose 함수 사용하여 행과 열을 바꿔줘야됨
df_vis = df1.T
# print(df_vis)
df_vis.columns = ["South", "North"]
# print(df_vis)

df_vis.plot.bar()
df_vis.plot.barh()
plt.show()
"""

"""
# sell_bike

df = pd.read_csv("sell_bike.csv", index_col='자전거매장', encoding="cp949")
# print(df.info())
# print(df)
# exit() # 이게 뭐하는 코든데?

df_sum = df.sum(axis=1)
df_sum.sort_values(axis=0, inplace=True)
# print(df_sum)


# df_sum.plot.barh()
df_sum.plot.barh(grid=True)
plt.xlim(2200, 3500)
# plt.show()

"""

"""
df = pd.read_csv("sell_bike_inc_kinds.csv", index_col='자전거매장', encoding='cp949')
# print(df)

# 지역별 판매량을 그래프로 표현
# df.plot.barh(color=["#000000", "#555555", "#AAAAAA"])
# plt.show()

# 자전거 종류별로 막대그래프 표현
# df_tran.plot.barh(color=["#000000", "#AAAAAA"])
# plt.show()

# 지역별, 종류별 누적 그래프를 하나의 차트에 표현 -> plt.subplots() 사용
df_tran = df.T
fig, axes = plt.subplots(nrows=2, ncols=1)
df.plot.barh(stacked=True, color=["#000000", "#555555", "#AAAAAA"], ax=axes[0])
df_tran.plot.barh(stacked=True, color=["#000000", "#AAAAAA"], ax=axes[1])
plt.show()
"""

df = pd.read_csv("../Data/sell_bike.csv", index_col="자전거매장", encoding="cp949")
# print(df)

index = [1, 2, 3, 4, 5, 6]
London = list(df.loc["런던"].values) # [358,118,769,636,196,293]
York = list(df.loc["요크"].values) # [557, 404, 533, 115, 989, 309]
# print(London)
# print(York)

l_450 = [] # [0, 0, 769, 636, 0, 0]

for val in London:
    if val >= 450:
        l_450.append(val)
    else:
        l_450.append(0)

y_450 = [val if val >= 450 else 0 for val in York]

print(l_450)
print(y_450)
plt.subplots(nrows=2, ncols=1, sharex=True)

# plt.subplot : 각 영역에 대해 셋팅
plt.subplot(2, 1, 1) # subplot(row, col, idx) : London 데이터
plt.bar(index, London, color="brown") # 전체가 갈색으로 그래프를 표현
plt.bar(index, l_450, color="orange") # [0, 0, 769, 636, 0, 0] 오렌지색으로 덮어씀
plt.legend(["No", "Yes"], loc='best') # 범례를 표현할 위치
plt.axhline(y=450, xmin=0, xmax=1, color="blue") # x축으로 y=450인 부분을 선으로 그음. x축은 비율로 계산
plt.ylabel("London")
plt.ylim(0, 1200)

plt.subplot(2, 1, 2) # subplot(row, col, idx) : York 데이터
plt.bar(index, York, color="brown") # 전체가 갈색으로 그래프를 표현
plt.bar(index, y_450, color="orange") # [557, 0, 533, 0, 989, 0] 오렌지색으로 덮어씀
plt.legend(["No", "Yes"], loc='best') # 범례를 표현할 위치
plt.axhline(y=450, xmin=0, xmax=1, color="blue") # x축으로 y=450인 부분을 선으로 그음. x축은 비율로 계산
plt.ylabel("York")
plt.ylim(0, 1200)

plt.show()

