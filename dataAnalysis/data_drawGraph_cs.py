import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
df = pd.read_csv("sell_bike.csv", encoding="cp949", index_col="자전거매장")
print(df)

# df_sum = df.sum(axis=1)
# print(df_sum)
#
# # 정렬하고싶어: sort_values
# df_sum.sort_values(axis=0, inplace=True)
# df_sum.plot.barh(grid=True)
#
# # 영점기준을 바꾸고싶어: xlim
# plt.xlim(2200, 3500)
#
# # 한칸당범위를 바꾸고싶어: xticks
# plt.xticks(list(range(2200, 3500, 100)))
# plt.show()

# 런던, 요크에서 목표치인 450대를 넘었는지 알고싶어
idx = [1, 2, 3, 4, 5, 6]
count_yes = 0
count_no = 0
London = list(df.loc["런던"].values)  # [358, 118, 769, 636, 196, 293]
York = list(df.loc["요크"].values)  # [557, 404, 533, 115, 989, 309]
L450 = []  # [0, 0, 769, 636, 0, 0]
Y450 = []
R450 = []
M450 = []
B450 = []
for val in London:
    if val >= 450:
        L450.append(val)
        count_yes += 1
    else:
        L450.append(0)
        count_no += 1
# Y450 = [val if val >= 450 else 0 for val in York]  # [557, 0, 533, 0, 989, 0]
for val in York:
    if val >= 450:
        Y450.append(val)
        count_yes += 1
    else:
        Y450.append(0)
        count_no += 1
Reeds = list(df.loc["리즈"].values)
Manch = list(df.loc["멘체스터"].values)
Birm = list(df.loc["버밍업"].values)
for val in Reeds:
    if val >= 450:
        R450.append(val)
        count_yes += 1
    else:
        R450.append(0)
        count_no += 1
for val in Manch:
    if val >= 450:
        M450.append(val)
        count_yes += 1
    else:
        M450.append(0)
        count_no += 1
for val in Birm:
    if val >= 450:
        B450.append(val)
        count_yes += 1
    else:
        B450.append(0)
        count_no += 1

count_list = [count_yes, count_no]
# plt.subplots(nrows=2, ncols=1, sharex=True)
# plt.subplot(2, 1, 1)  # subplot(row, col, idx)
# plt.bar(idx, London, color="brown")
# plt.bar(idx, L450, color="orange")
# plt.legend(["No", "Yes"], loc='best')
# plt.axhline(y=450, xmin=0, xmax=1, color="skyblue")
# plt.ylabel("London")
# plt.ylim(0, 1200)
# plt.subplot(2, 1, 2)
# plt.bar(idx, York, color="brown")
# plt.bar(idx, Y450, color="orange")
# plt.axhline(y=450, xmin=0, xmax=1, color="skyblue")
# plt.ylabel("York")
# plt.ylim(0, 1200)
# plt.show()

plt.figure(figsize=(10, 4))
plt.barh(["yes"], count_list[0], color="orange", height=0.6)
plt.barh(["no"], count_list[1], color="brown", height=0.6)
plt.xticks(range(0, 21, 2))
plt.show()

# df = pd.read_csv("sell_bike_inc_kinds.csv", encoding="cp949", index_col="자전거매장")
# print(df)
# df.plot.barh()
# plt.show()
#
# # 흑백으로 바꾸고싶어
# df.plot.barh(color=["black", "gray", "lightgray"])
# plt.show()
#
# # 자전거 종류별로 보고싶어
# df_trans = df.T
# print(df_trans)
# df_trans.plot.barh(color=["black", "gray"])
# plt.show()
#
# # 지역별, 종류별 누적 그래프를 하나의 차트에 표현
# plt.subplots
# df_trans = df.T
# fig, axis = plt.subplots(nrows=2, ncols=1)
# df.plot.barh(color=["black", "gray", "lightgray"], stacked=True, ax=axis[0])
# df_trans.plot.barh(color=["black", "gray"], stacked=True, ax=axis[1])
# plt.show()
