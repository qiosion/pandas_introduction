import pandas as pd
import seaborn as sns

#데이터프레임 vs 숫자 연산 -> 타이타닉 데이터를 이용해보자!
pd.set_option('display.max_columns', None) # 모든 칼럼 확인가능

titanic = sns.load_dataset('titanic') # 타이타닉 데이터를 불러옴
print(titanic.head())

# 모든 행과 두개의 열(나이 age, 티켓요금 fare)을 가져오고 싶다
df = titanic.loc[:, ['age', 'fare']]
# print(df)
addition = df + 10
print(addition.head())

# 데이터프레임 vs 데이터프레임 연산
substraction = addition - df
print(substraction.head())
