import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df_titanic = sns.load_dataset('titanic')
print(df_titanic.info())
# print(df_titanic.head()) # end="\n" : 디폴트로 개행문자 들어감
print() # 엔터값과 동일

# 디폴트 : value_counts(dropna=True) # NaN을 드랍한 뒤, 남은 데이터의 요소 값을 카운트하여 반환
print(df_titanic['deck'].value_counts(dropna=False))

# isnull() : 누락데이터면 True 반환. 유효 데이터가 존재하면 False 반환
print(df_titanic.head().isnull())
print("all >>>")
print(df_titanic.isnull().all())
print("any >>>")
print(df_titanic.isnull().any())
print("df에 하나라도 NaN이 있으면 True를 반환하고 싶을 때 >>>")
# df에 하나라도 NaN이 있으면 True를 반환하고 싶을 때
print(df_titanic.isnull().any().any())

# 각각의 열에서 NaN가 몇개인지 카운트하여 반환
print(df_titanic.isnull().sum())
print(df_titanic.isnull().sum(axis=0)) # col 기준
print(df_titanic.isnull().sum(axis=1)) # row 기준

print("count >>>")
print(df_titanic.count())

# drop 실습
# deck 열에는 NaN가 너무 많다 -> 일반적으로 이런 케이스는 날려주는게 좋다
df_drop = df_titanic.drop(columns=['deck'])
print(df_drop.head())

# 칼럼 기준 NaN가 500개 이상이면 drop 해줘
df_thresh = df_titanic.dropna(axis=1, thresh=500)
print(df_thresh.head())

# dropna : age 열에서 NaN 값이 있는 "행"을 삭제
df_age = df_titanic.dropna(subset=['age'], axis=0)
df_age_any = df_titanic.dropna(subset=['age', 'deck'], axis=0, how='any')
# how 옵션 all, any
# how = all : subset에 있는 컬럼들이 모두 NaN일 경우, 해당 행을 삭제
# how = any : subset에 있는 컬럼들 중 하나라도 NaN일 경우, 해당 행을 삭제
print(len(df_age))

# fillna
mean_age = df_titanic['age'].mean()
df_fillna = df_titanic['age'].fillna(mean_age)
print("평균 나이 : ", mean_age)
print("NaN을 평균나이로 대체", df_fillna)

# ffill : Forward fill : 앞 또는 위의 데이터로부터 NaN을 채우는 방식
# bfill : Backward fill : 뒤 또는 밑의 데이터로부터 NaN을 채우는 방식


# mask를 사용해서, True인 데이터만 가지고 오고싶음
df_titanic.embark_town.isnull() # 모든 행에 대해 True 또는 False 로 결과가 나온다

# 데이터 프레임에서 주어진 조건 중 isnull 이 True인 값만 가져온다
# -> embark_town 이 NaN인 두개의 행만 가져옴
print(df_titanic[df_titanic.embark_town.isnull()])

df_ffill = df_titanic['embark_town'].fillna(method='ffill')
print(df_ffill[825:])