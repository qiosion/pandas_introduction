import pandas as pd
import numpy as np


# 모든 칼럼 확인가능
pd.set_option('display.max_columns', None)

df_pokemon = pd.read_csv("../Data/Pokemon.csv")
# df_pokemon = pd.read_csv("../Data/Pokemon.csv", header=1)

# print(df_pokemon)
# print(df_pokemon.columns)

# 1번.
# Attack 칼럼을 기준으로 내림차순 정렬
# Attack = 인덱스번호 6
df_sorted = df_pokemon.sort_values(by ='Attack', ascending=False)
print(df_sorted)

# 상위 400위 포켓몬
top_400 = df_sorted.head(400)

# 401~800위 포켓몬
next_400 = df_sorted.iloc[400:800]

# 상위 400위 포켓몬에서 전설 포켓몬의 숫자
# Legendary = 인덱스번호 12
top_legendary = top_400['Legendary'].sum()

# 401~800위 포켓몬에서 전설 포켓몬의 숫자
next_legendary = next_400['Legendary'].sum()

# 전설 포켓몬 숫자 차이 계산
legendary_gap = top_legendary - next_legendary

print("상위 400위 포켓몬 중 전설 포켓몬의 수:", top_legendary)
print("401~800위 포켓몬 중 전설 포켓몬의 수:", next_legendary)
print("상위 400위와 401~800위 포켓몬들에서 전설 포켓몬의 숫자 차이:", legendary_gap)

# 2번.
# Type 1 = 인덱스번호 2
fire_pokemon = df_pokemon[df_pokemon.iloc[:, 2] == 'Fire']
# fire_mean = fire_pokemon[6].astype(int).mean()
fire_mean = fire_pokemon.iloc[:, 6].astype(int).mean()

water_pokemon = df_pokemon[(df_pokemon.iloc[:, 2] == 'Water') & (df_pokemon.iloc[:, 6].astype(int) > fire_mean)]
water_count = water_pokemon.shape[0]

print("Fire 속성 포켓몬의 Attack 평균:", fire_mean) # 84.76923076923077
print("Attack 평균 이상인 Water 속성 포켓몬의 수:", water_count) # 37

df_bank = pd.read_csv("../Data/bank.csv", delimiter=';', skiprows=0)

# 3번.
# 나이를 10살 단위로 변환하는 함수
def convert_age(age):
    return (age // 10) * 10

    # 나이를 10살 단위로 변환
df_bank['age'] = df_bank['age'].apply(convert_age)

most_common_age = df_bank['age'].value_counts().idxmax()
num_people = df_bank['age'].value_counts().max()

print("가장 많은 인원을 가진 나이대:", most_common_age)
print("인원수:", num_people)

# 4번.
# 'age' 행 제거
df_bank = df_bank[df_bank.iloc[:, 0] != 'age']

# 나이가 25살 이상 29살 미만
# housing이 "yes"인 고객의 수
filtered_customers = df_bank[(df_bank['age'] >= 25) & (df_bank['age'] < 29) & (df_bank['housing'] == 'yes')]
# filtered_customers = df_bank[(df_bank.iloc[:, 0].astype(int) >= 25) & (df_bank.iloc[:, 0].astype(int) < 29) & (df_bank.iloc[:, 6] == 'yes')]
customers_cnt = len(filtered_customers)

print("나이가 25세 이상 29세 미만인 응답 고객 중 housing이 'yes'인 고객의 수:", customers_cnt)

# 5번.
# numeric한 값을 가지지 않은 칼럼
non_numeric = df_bank.select_dtypes(exclude=[int, float])

max_count = 0
unique_column = None

for column in non_numeric:
    unique_count = df_bank[column].nunique()

    if unique_count > max_count:
        max_count = unique_count
        unique_column = column

print("가장 unique한 칼럼 :", unique_column)
print("Unique한 값의 개수 :", max_count)

# 6번.
# 평균
balance_mean = df_bank['balance'].mean()

overed = df_bank[df_bank['balance'] >= balance_mean]

filtered_data = overed.sort_values(by='balance', ascending=False)
top_100_balance = filtered_data.head(100)['balance'].mean()
print("상위 100개 balance 값의 평균:", top_100_balance)

df_bank = pd.read_csv("../Data/bank.csv", delimiter=';')

# 7번.
# 'day'와 'month' 칼럼을 기준으로 그룹화하여 집계
df_bank['date'] = df_bank['day'].astype(str) + ', ' + df_bank['month']

# 안받은사람 필터링
filtered_df = df_bank[df_bank['contact'] != 'unknown']

# 가장 많은 마케팅 집행 건수를 가진 날짜를 찾음
most_common_date = filtered_df['date'].value_counts().idxmax()

# 결과 출력
print("가장 많이 마케팅을 집행한 날짜 :", most_common_date)

# 8번.
# age와 balance 칼럼 간의 상관계수 계산
correlation = df_bank['age'].corr(df_bank['balance'])

print("age와 balance 칼럼 간의 상관계수 :", correlation) # 0.08382014224477764

correlation_matrix = df_bank[['age', 'balance']].corr()
# 상관계수 행렬을 NumPy 배열로 변환
correlation_array = np.array(correlation_matrix)

print(">>> 상관계수 행렬")
print(correlation_array)

df_stroke = pd.read_csv("../Data/healthcare-dataset-stroke-data.csv")
# df_stroke = pd.read_csv("../Data/healthcare-dataset-stroke-data.csv", header=None)
print(df_stroke)

"""
# 9번.
male_patients = df_stroke[df_stroke['gender'] == 'Male']
average_age = round(male_patients['age'].mean(), 3)

print("Male 환자들의 평균 나이 : ", average_age) # 42.483
"""

# 10번.
# 결측치를 평균값으로 채우기
mean_bmi = df_stroke['bmi'].mean()
df_stroke['bmi'].fillna(mean_bmi, inplace=True)

# 'bmi' 열의 평균 계산
average_bmi = round(df_stroke['bmi'].mean(), 3)

print('bmi 칼럼의 평균값 : ', average_bmi) # 28.893