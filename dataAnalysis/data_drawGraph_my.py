import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
# df = pd.read_csv('sell_bike_inc_kinds.csv', index_col="자전거매장", encoding='cp949')
df = pd.read_csv('sell_bike.csv', index_col="자전거매장", encoding='cp949')
print(df.head())
# print(df.values)
list_up_450 = []
list_down_450 = []

for i in df.values:
    print(i)

for i in df.values:
    for j in i:
        if (j>=450):
            list_up_450.append(j)

for i in df.values:
    for j in i:
        if (j < 450):
            list_down_450.append(j)

list_show = [len(list_up_450)]  + [len(list_down_450)]
#확인차에
print(list_show)
#겹칠 거
list_yes = [len(list_up_450)] + [0] #[0]는 겹치는 거.
print(list_yes)

input = ['Yes', 'No']
plt.barh(input, list_show, color='orange')
plt.barh(input, list_yes, color= 'brown')
plt.show()

    # list.append(val if val >= 450 else 0 for val in i)
# print("450 이상 리스트를 출력:" , list_up_450)
# print("450 미만 리스트 출력 : ", list_down_450)
# print(len(list_up_450))
# count_y = len(list_up_450)
# print(len(list_down_450))
# count_n = len(list_down_450)
# input = ['yes', 'no']
# plt.barh( input, count_y, color = 'brown')
# # plt.barh(input, count_n, color = 'orange')
# plt.show()


